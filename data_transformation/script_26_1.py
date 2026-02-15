"""
Author: Sharad Jadhav
Category: Data Transformation
Task: Clean column names for SQL.
"""

def clean_cols(cols):
    return [c.strip().lower().replace(' ', '_') for c in cols]