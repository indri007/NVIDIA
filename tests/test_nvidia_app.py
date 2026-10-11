import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import pytest
from scripts.digital_observation import (
    load_tiktok_observation,
    load_financial_social_df,
    load_gap_analysis,
    load_iceberg_dimensions,
    load_rhwr_framework,
    compute_silent_authority_index,
    evaluate_rhwr_filter
)


def test_tiktok_observation_structure():
    data = load_tiktok_observation()
    assert "paper_reference" in data
    assert "accounts" in data
    assert len(data["accounts"]) >= 3
    handles = [acc["handle"] for acc in data["accounts"]]
    assert "@nvidia" in handles
    assert "@nvidiageforce" in handles


def test_financial_social_dataframe():
    df = load_financial_social_df()
    assert not df.empty
    assert "fiscal_year" in df.columns
    assert "revenue_usd_billion" in df.columns
    assert "cuda_developers_million" in df.columns
    # Check FY26 record
    fy26_row = df[df["fiscal_year"] == "FY26"].iloc[0]
    assert fy26_row["revenue_usd_billion"] == 215.90
    assert fy26_row["tiktok_corp_uploads"] == 0


def test_gap_analysis_dimensions():
    gap_list = load_gap_analysis()
    assert len(gap_list) == 5
    dims = [item["dimensi"] for item in gap_list]
    assert "Kehadiran Digital" in dims
    assert "Metrik Keberhasilan" in dims
    assert "Arsitektur Teknologi" in dims
    assert "Geopolitik & Regulasi" in dims
    assert "Budaya Organisasi" in dims


def test_iceberg_dimensions():
    iceberg = load_iceberg_dimensions()
    assert "visible_layer" in iceberg
    assert "invisible_layer" in iceberg
    assert len(iceberg["visible_layer"]["elements"]) == 3
    assert len(iceberg["invisible_layer"]["elements"]) == 5


def test_rhwr_framework():
    rhwr = load_rhwr_framework()
    assert len(rhwr["pillars"]) == 4
    assert len(rhwr["case_scenarios"]) >= 3


def test_compute_silent_authority_index():
    # NVIDIA standard case
    res = compute_silent_authority_index(
        revenue_billion=215.90,
        market_cap_trillion=3.45,
        cuda_developers_million=6.2,
        corporate_tiktok_uploads=0,
        corporate_tiktok_followers=0
    )
    assert res["silent_authority_index"] > 85.0
    assert res["classification"] == "Absolute Silent Authority"

    # Social media dependent influencer brand case
    res_influencer = compute_silent_authority_index(
        revenue_billion=0.05,
        market_cap_trillion=0.001,
        cuda_developers_million=0.01,
        corporate_tiktok_uploads=500,
        corporate_tiktok_followers=5000000
    )
    assert res_influencer["silent_authority_index"] < 40.0
    assert res_influencer["classification"] == "Dopamine-Dependent Branding"


def test_rhwr_evaluation():
    # Perfect score
    res_full = evaluate_rhwr_filter(True, True, True, True)
    assert res_full["passed_pillars"] == 4
    assert res_full["status"] == "APPROVED_ROBUST"

    # 1 fail
    res_warning = evaluate_rhwr_filter(True, True, False, True)
    assert res_warning["passed_pillars"] == 3
    assert res_warning["status"] == "CONDITIONAL_APPROVAL"

    # High risk
    res_rejected = evaluate_rhwr_filter(False, False, True, False)
    assert res_rejected["passed_pillars"] == 1
    assert res_rejected["status"] == "HIGH_RISK_REJECTED"


def test_pdf_paper_exists():
    pdf_filename = "View of Silent Authority dan Paradigma Branding Iceberg_ Analisis Strategi Komunikasi Digital NVIDIA di Platform TikTok dalam Era Marketing 5.0.pdf"
    full_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), pdf_filename)
    assert os.path.isfile(full_path), f"PDF file not found at {full_path}"
    assert os.path.getsize(full_path) > 4000000, "PDF file is unexpectedly small"
