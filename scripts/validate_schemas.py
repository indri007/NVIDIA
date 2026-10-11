#!/usr/bin/env python3
"""
F7: Schema Validation & Data Integrity Suite
Validates all raw and processed CSV datasets against the PRD data dictionary.
"""

import os
import pandas as pd
import hashlib
from typing import Dict, List, Tuple

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
EVIDENCE_DIR = os.path.join(BASE_DIR, "evidence")

SCHEMAS = {
    "snapshots_account.csv": {
        "required_cols": [
            "account_id", "platform", "handle", "captured_at_utc",
            "followers", "following", "likes", "video_count",
            "verified", "bio", "evidence_file", "sha256"
        ],
        "non_null_cols": ["account_id", "platform", "handle", "captured_at_utc", "sha256"],
        "min_rows": 10
    },
    "comparison_accounts.csv": {
        "required_cols": [
            "company", "sector", "business_model", "platform",
            "handle", "presence_type", "coder_1", "coder_2", "notes"
        ],
        "non_null_cols": ["company", "platform", "handle", "presence_type", "coder_1", "coder_2"],
        "valid_values": {
            "presence_type": ["active", "dormant", "placeholder", "defensive"]
        },
        "min_rows": 15
    },
    "lookalike_accounts.csv": {
        "required_cols": ["brand", "platform", "handle", "found_at", "reason", "status"],
        "non_null_cols": ["brand", "platform", "handle", "reason"],
        "min_rows": 5
    },
    "third_party_series.csv": {
        "required_cols": ["source", "query", "week_start", "volume", "sentiment_score"],
        "non_null_cols": ["source", "query", "week_start", "volume"],
        "min_rows": 20
    },
    "documents_coded.csv": {
        "required_cols": ["doc_id", "type", "date", "code", "coder", "excerpt_ref"],
        "non_null_cols": ["doc_id", "code", "coder", "excerpt_ref"],
        "min_rows": 8
    }
}


def validate_all_schemas() -> Tuple[bool, List[str]]:
    """Validates all CSV tables against required columns, nullness, and constraints."""
    errors = []
    
    for filename, rules in SCHEMAS.items():
        filepath = os.path.join(PROCESSED_DIR, filename)
        if not os.path.exists(filepath):
            errors.append(f"Missing file: {filename}")
            continue
        
        df = pd.read_csv(filepath)
        
        # Check min rows
        if len(df) < rules.get("min_rows", 1):
            errors.append(f"{filename}: expected at least {rules['min_rows']} rows, got {len(df)}")
        
        # Check required columns
        missing_cols = [c for c in rules["required_cols"] if c not in df.columns]
        if missing_cols:
            errors.append(f"{filename}: missing columns {missing_cols}")
        
        # Check non-null columns
        for c in rules["non_null_cols"]:
            if c in df.columns and df[c].isnull().any():
                null_count = df[c].isnull().sum()
                errors.append(f"{filename}: column '{c}' contains {null_count} null values")
        
        # Check valid value sets
        if "valid_values" in rules:
            for c, allowed in rules["valid_values"].items():
                if c in df.columns:
                    invalid = set(df[c].dropna().unique()) - set(allowed)
                    if invalid:
                        errors.append(f"{filename}: invalid values in '{c}': {invalid}")
    
    # Check SHA-256 evidence integrity
    snap_path = os.path.join(PROCESSED_DIR, "snapshots_account.csv")
    if os.path.exists(snap_path):
        df_snaps = pd.read_csv(snap_path)
        for _, row in df_snaps.iterrows():
            ev_rel = row["evidence_file"]
            ev_full = os.path.join(EVIDENCE_DIR, ev_rel)
            if not os.path.exists(ev_full):
                errors.append(f"Evidence file missing: {ev_rel}")
            else:
                with open(ev_full, "rb") as f:
                    actual_sha = hashlib.sha256(f.read()).hexdigest()
                if actual_sha != row["sha256"]:
                    errors.append(f"SHA-256 mismatch for {ev_rel}: expected {row['sha256']} but got {actual_sha}")

    is_valid = len(errors) == 0
    return is_valid, errors


if __name__ == "__main__":
    valid, errs = validate_all_schemas()
    if valid:
        print("✅ ALL SCHEMAS & EVIDENCE SHA-256 CHECKS PASSED (F7 Compliant)")
    else:
        print("❌ SCHEMA VALIDATION FAILED:")
        for e in errs:
            print(f"  - {e}")
        exit(1)
