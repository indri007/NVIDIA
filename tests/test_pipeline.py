"""
Unit test suite for Analysis Pipeline and Inter-Coder Reliability (F4/F6).
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.compute_krippendorff import evaluate_study_reliability
from scripts.run_analysis import run_full_analysis


def test_intercoder_reliability():
    res = evaluate_study_reliability()
    assert res["all_passed"], "Inter-coder reliability failed standard acceptance criteria"
    assert res["alpha_accounts"] >= 0.70, f"Account alpha too low: {res['alpha_accounts']}"
    assert res["alpha_documents"] >= 0.70, f"Document alpha too low: {res['alpha_documents']}"


def test_analysis_output_artifacts():
    run_full_analysis()
    
    # Check tables
    tab_dir = os.path.join(BASE_DIR, "paper", "tables")
    assert os.path.exists(os.path.join(tab_dir, "table1_presence_distribution.csv"))
    assert os.path.exists(os.path.join(tab_dir, "table2_lookalike_summary.csv"))
    assert os.path.exists(os.path.join(tab_dir, "table3_third_party_compensation.csv"))
    assert os.path.exists(os.path.join(tab_dir, "table4_hypothesis_test_results.csv"))
    
    # Check figures
    fig_dir = os.path.join(BASE_DIR, "paper", "figures")
    assert os.path.exists(os.path.join(fig_dir, "figure1_longitudinal_trajectory.png"))
    assert os.path.exists(os.path.join(fig_dir, "figure2_presence_by_sector.png"))
    assert os.path.exists(os.path.join(fig_dir, "figure3_third_party_volume.png"))
