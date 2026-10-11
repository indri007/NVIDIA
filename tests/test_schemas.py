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
