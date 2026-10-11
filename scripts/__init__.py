"""
Silent Authority & Branding Iceberg Scripts Package.
If executed directly by Streamlit as main module (e.g. on Streamlit Cloud),
this safely delegates execution to the primary app.py dashboard.
"""
import os
import sys
import runpy

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

APP_PATH = os.path.join(ROOT_DIR, "app.py")
if os.path.exists(APP_PATH):
    runpy.run_path(APP_PATH, run_name="__main__")
