#!/usr/bin/env python3
"""
F1 & F2: Automated Snapshot Logging & Evidence Archiving
Demonstrates reproducible logging of digital profiles with UTC timestamp and SHA-256 evidence hashing.
"""

import os
import hashlib
import datetime
import pandas as pd
from typing import Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
EVIDENCE_DIR = os.path.join(BASE_DIR, "evidence")


def record_account_snapshot(
    account_id: str,
    platform: str,
    handle: str,
    followers: int,
    following: int,
    likes: int,
    video_count: int,
    verified: bool,
    bio: str,
    evidence_filename: str
) -> Dict[str, Any]:
    """Records a new snapshot with calculated SHA-256 hash."""
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ev_full = os.path.join(EVIDENCE_DIR, evidence_filename)
    
    if os.path.exists(ev_full):
        with open(ev_full, "rb") as f:
            sha = hashlib.sha256(f.read()).hexdigest()
    else:
        sha = "MISSING_EVIDENCE_FILE"
    
    record = {
        "account_id": account_id,
        "platform": platform,
        "handle": handle,
        "captured_at_utc": now_utc,
        "followers": followers,
        "following": following,
        "likes": likes,
        "video_count": video_count,
        "verified": verified,
        "bio": bio,
        "evidence_file": evidence_filename,
        "sha256": sha
    }
    return record


if __name__ == "__main__":
    print("Snapshot Logging Engine (F1/F2)")
    rec = record_account_snapshot(
        account_id="ACC_NV_CORP",
        platform="TikTok",
        handle="@nvidia",
        followers=0,
        following=0,
        likes=0,
        video_count=0,
        verified=True,
        bio="Official NVIDIA TikTok account.",
        evidence_filename="screenshots/nvidia_tiktok_20261011.png"
    )
    print("Sample Recorded Snapshot:")
    for k, v in rec.items():
        print(f"  {k}: {v}")
