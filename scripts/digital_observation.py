#!/usr/bin/env python3
"""
Digital Observation & Branding Iceberg Pipeline
Author: Based on research by Indri Anjar Kartika Sari, Agung Budi Prasetio, Waspodo Tjipto Subroto (IPSSJ 2026)
Repository: https://github.com/indri007/NVIDIA
"""

import json
import os
import pandas as pd
from typing import Dict, Any, List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_tiktok_observation() -> Dict[str, Any]:
    """Load empirical observation data of NVIDIA TikTok and broadcast accounts."""
    path = os.path.join(DATA_DIR, "tiktok_observation.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_financial_social_df() -> pd.DataFrame:
    """Load financial performance vs social media vanity metrics time series."""
    path = os.path.join(DATA_DIR, "financial_vs_social.csv")
    return pd.read_csv(path)


def load_gap_analysis() -> List[Dict[str, Any]]:
    """Load the 5-dimensional gap analysis (Public Expectation 10% vs Strategic Reality 90%)."""
    path = os.path.join(DATA_DIR, "gap_analysis.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_iceberg_dimensions() -> Dict[str, Any]:
    """Load 10% visible vs 90% invisible iceberg taxonomy."""
    path = os.path.join(DATA_DIR, "iceberg_dimensions.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_rhwr_framework() -> Dict[str, Any]:
    """Load the RHWR (Rational, Healthy, Wise, Right) crisis communication framework."""
    path = os.path.join(DATA_DIR, "rhwr_framework.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def compute_silent_authority_index(
    revenue_billion: float = 215.90,
    market_cap_trillion: float = 3.45,
    cuda_developers_million: float = 6.2,
    corporate_tiktok_uploads: int = 0,
    corporate_tiktok_followers: int = 0
) -> Dict[str, Any]:
    """
    Computes the Silent Authority Index (SAI).
    Demonstrates the inverted correlation between industrial economic hegemony
    and reliance on short-form social media vanity metrics.
    """
    # Normalized industrial gravity (scale 0-100)
    # Target benchmark: $200B+ revenue, $3T+ market cap, 6M+ CUDA devs
    fin_score = min(100.0, (revenue_billion / 220.0) * 50.0 + (market_cap_trillion / 3.5) * 50.0)
    moat_score = min(100.0, (cuda_developers_million / 6.5) * 100.0)
    substance_score = (fin_score * 0.5) + (moat_score * 0.5)

    # Vanity dependency score (0 = zero reliance on dopamine algorithms)
    vanity_score = min(100.0, (corporate_tiktok_uploads * 2.0) + (corporate_tiktok_followers / 50000.0))

    # Silent Authority Quotient: Substance / (1 + Vanity Dependency)
    sai_score = substance_score / (1.0 + (vanity_score / 50.0))

    # Interpretive classification
    if sai_score >= 85:
        category = "Absolute Silent Authority"
        desc = "Hegemoni substansial total; kehadiran digital berfungsi sebagai jangkar defensif identitas hukum tanpa ketergantungan pada viralitas."
    elif sai_score >= 60:
        category = "High Strategic Authority"
        desc = "Otoritas struktural kuat dengan interaksi media sosial selektif pada lini produk tertentu."
    elif sai_score >= 40:
        category = "Balanced Engagement"
        desc = "Keseimbangan antara performa komersial dan interaksi media sosial dua arah."
    else:
        category = "Dopamine-Dependent Branding"
        desc = "Ketergantungan tinggi pada algoritma viralitas dan sentimen publik jangka pendek."

    return {
        "silent_authority_index": round(sai_score, 2),
        "substance_score": round(substance_score, 2),
        "financial_dominance_score": round(fin_score, 2),
        "ecosystem_moat_score": round(moat_score, 2),
        "vanity_dependency_score": round(vanity_score, 2),
        "classification": category,
        "interpretation": desc
    }


def evaluate_rhwr_filter(
    rational: bool,
    healthy: bool,
    wise: bool,
    right: bool
) -> Dict[str, Any]:
    """
    Evaluates whether a crisis response passes the RHWR protocol filter.
    Returns composite score, status, and targeted recommendations.
    """
    checks = {
        "Rational (Bukti Empiris & Data)": rational,
        "Healthy (Keberlanjutan Ekosistem)": healthy,
        "Wise (Sensitivitas Geopolitik)": wise,
        "Right (Etika & Kepatuhan Regulasi)": right
    }
    passed_count = sum(1 for v in checks.values() if v)
    score_pct = (passed_count / 4.0) * 100.0

    if passed_count == 4:
        status = "APPROVED_ROBUST"
        verdict = "Lolos 100% Protokol RHWR: Respon komunikasi memiliki integritas data, menjaga ekosistem, bijak secara geopolitik, dan patuh etika."
        color = "green"
    elif passed_count == 3:
        status = "CONDITIONAL_APPROVAL"
        verdict = "Peringatan Mitigasi: 1 pilar gagal dipenuhi. Wajib penyesuaian narasi sebelum publikasi resmi."
        color = "yellow"
    else:
        status = "HIGH_RISK_REJECTED"
        verdict = "Ditolak: Respon berisiko tinggi memperlebar Interpretation Gap dan merusak wibawa korporat."
        color = "red"

    return {
        "score_percent": score_pct,
        "passed_pillars": passed_count,
        "total_pillars": 4,
        "status": status,
        "verdict": verdict,
        "color": color,
        "checks": checks
    }


def run_cli_diagnostic() -> None:
    """Print an executive summary of the digital observation pipeline."""
    print("=" * 70)
    print("NVIDIA DIGITAL OBSERVATION & SILENT AUTHORITY PIPELINE")
    print("Reference: IPSSJ Vol. 3 No. 9 2026 (Sari, Prasetio, & Subroto)")
    print("=" * 70)

    obs = load_tiktok_observation()
    print(f"\n[1] Observasi Akun TikTok:")
    for acc in obs["accounts"]:
        print(f"  - {acc['handle']} ({acc['platform']}): {acc['account_type']}")
        print(f"    Followers: {acc['followers']:,} | Uploads: {acc['uploads_count']} | Peran: {acc['strategic_purpose']}")

    df = load_financial_social_df()
    print(f"\n[2] Waktu & Metrik Finansial vs Media Sosial:")
    print(df[["fiscal_year", "revenue_usd_billion", "datacenter_rev_percent", "cuda_developers_million", "tiktok_corp_uploads"]].to_string(index=False))

    sai = compute_silent_authority_index()
    print(f"\n[3] Silent Authority Index (SAI):")
    print(f"  Score: {sai['silent_authority_index']}/100 | Klasifikasi: {sai['classification']}")
    print(f"  Penjelasan: {sai['interpretation']}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    run_cli_diagnostic()
