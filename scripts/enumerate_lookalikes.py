#!/usr/bin/env python3
"""
F3: Lookalike & Brand Squatting Enumeration
Analyzes potential cybersquatting, typosquatting, and impersonator candidates.
"""

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")


def audit_lookalike_inventory() -> pd.DataFrame:
    """Loads and computes summary statistics on lookalike accounts."""
    look_path = os.path.join(PROCESSED_DIR, "lookalike_accounts.csv")
    df = pd.read_csv(look_path)
    return df


if __name__ == "__main__":
    df = audit_lookalike_inventory()
    print("=" * 60)
    print(f"LOOKALIKE & SQUATTING ENUMERATION AUDIT (N={len(df)})")
    print("=" * 60)
    print(df[["brand", "handle", "status", "reason"]].to_string(index=False))
