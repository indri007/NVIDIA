"""
Unit test suite for Dataset Schemas and Integrity (F7).
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.validate_schemas import validate_all_schemas


def test_dataset_schemas_and_hashes():
    valid, errors = validate_all_schemas()
    assert valid, f"Schema validation failed with errors: {errors}"
    assert len(errors) == 0


def test_erd_documentation_exists():
    erd_path = os.path.join(BASE_DIR, "docs", "ERD.md")
    assert os.path.isfile(erd_path), f"ERD documentation not found at {erd_path}"
    with open(erd_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Verify core entities are documented in ERD
    required_entities = [
        "COMPANY",
        "CORPORATE_ACCOUNT",
        "ACCOUNT_SNAPSHOT",
        "AUDIT_EVIDENCE",
        "PRESENCE_BENCHMARK_CODING",
        "LOOKALIKE_ACCOUNT",
        "THIRD_PARTY_METRICS",
        "CODED_DOCUMENT",
        "THEMATIC_SEGMENT_CODING",
        "FINANCIAL_MACRO_METRICS"
    ]
    for entity in required_entities:
        assert entity in content, f"Entity {entity} not found in ERD documentation"

