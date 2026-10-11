#!/usr/bin/env python3
"""
F4: Inter-Coder Reliability Evaluation
Computes Krippendorff's alpha (nominal) for double-coded accounts and thematic documents.
"""

import os
import sys
import pandas as pd
import numpy as np

# Discover fast-krippendorff library
FAST_KRIPP_SRC = "/Users/jevin/research-tools/fast-krippendorff/src"
if os.path.exists(FAST_KRIPP_SRC) and FAST_KRIPP_SRC not in sys.path:
    sys.path.insert(0, FAST_KRIPP_SRC)

try:
    import krippendorff
    HAS_KRIPPENDORFF_PKG = True
except ImportError:
    HAS_KRIPPENDORFF_PKG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")


def calculate_nominal_alpha(coder1_labels: list, coder2_labels: list) -> float:
    """Calculate Krippendorff's Alpha for two coders using nominal metric."""
    unique_categories = sorted(list(set(coder1_labels + coder2_labels)))
    cat_to_id = {cat: i for i, cat in enumerate(unique_categories)}
    
    c1_numeric = [cat_to_id[c] for c in coder1_labels]
    c2_numeric = [cat_to_id[c] for c in coder2_labels]
    
    matrix = np.array([c1_numeric, c2_numeric])
    
    if HAS_KRIPPENDORFF_PKG:
        return float(krippendorff.alpha(reliability_data=matrix, level_of_measurement="nominal"))
    
    # Fallback exact mathematical formulation for 2 coders nominal data
    n_items = len(coder1_labels)
    agreements = sum(1 for a, b in zip(coder1_labels, coder2_labels) if a == b)
    observed_agreement = agreements / n_items
    
    # Marginal distribution expected agreement
    counts = {}
    for item in coder1_labels + coder2_labels:
        counts[item] = counts.get(item, 0) + 1
    total_ratings = 2 * n_items
    expected_agreement = sum((c / total_ratings) ** 2 for c in counts.values())
    
    if expected_agreement >= 1.0:
        return 1.0
    alpha = (observed_agreement - expected_agreement) / (1.0 - expected_agreement)
    return round(float(alpha), 4)


def evaluate_study_reliability():
    """Evaluates inter-coder reliability across comparison accounts and document coding."""
    print("=" * 70)
    print("KRIPPENDORFF'S ALPHA INTER-CODER RELIABILITY AUDIT (F4)")
    print("Target Threshold: Alpha >= 0.70 (Standard), Alpha >= 0.80 (Robust Q1)")
    print("=" * 70)
    
    # 1. Comparison Accounts Coding (D2)
    comp_path = os.path.join(PROCESSED_DIR, "comparison_accounts.csv")
    df_comp = pd.read_csv(comp_path)
    alpha_comp = calculate_nominal_alpha(df_comp["coder_1"].tolist(), df_comp["coder_2"].tolist())
    sample_size_comp = len(df_comp)
    raw_agreement_comp = (df_comp["coder_1"] == df_comp["coder_2"]).mean() * 100
    
    print(f"\n[1] Comparison Accounts Presence Typology (N={sample_size_comp}):")
    print(f"    Raw Agreement: {raw_agreement_comp:.1f}%")
    print(f"    Krippendorff's Alpha: {alpha_comp:.4f}")
    status_comp = "ROBUST (>= 0.80)" if alpha_comp >= 0.80 else ("ACCEPTABLE (>= 0.70)" if alpha_comp >= 0.70 else "FAIL")
    print(f"    Status: {status_comp}")
    
    # 2. Document Thematic Coding (D5)
    doc_path = os.path.join(PROCESSED_DIR, "documents_coded.csv")
    df_doc = pd.read_csv(doc_path)
    # Group by doc_id to align coder_1 and coder_2
    pivot = df_doc.pivot(index="excerpt_ref", columns="coder", values="code").dropna()
    alpha_doc = calculate_nominal_alpha(pivot["coder_1"].tolist(), pivot["coder_2"].tolist())
    raw_agreement_doc = (pivot["coder_1"] == pivot["coder_2"]).mean() * 100
    
    print(f"\n[2] Corporate & Technological Document Thematic Coding (N={len(pivot)}):")
    print(f"    Raw Agreement: {raw_agreement_doc:.1f}%")
    print(f"    Krippendorff's Alpha: {alpha_doc:.4f}")
    status_doc = "ROBUST (>= 0.80)" if alpha_doc >= 0.80 else ("ACCEPTABLE (>= 0.70)" if alpha_doc >= 0.70 else "FAIL")
    print(f"    Status: {status_doc}")
    
    print("\n" + "=" * 70)
    passed_all = (alpha_comp >= 0.70) and (alpha_doc >= 0.70)
    return {
        "alpha_accounts": alpha_comp,
        "alpha_documents": alpha_doc,
        "all_passed": passed_all
    }


if __name__ == "__main__":
    res = evaluate_study_reliability()
    if not res["all_passed"]:
        exit(1)
