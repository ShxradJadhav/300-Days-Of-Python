"""
Author: Sharad Jadhav
Date: 2026-01-30
Task: Format SQL query string for daily data extraction.
"""

def get_query(table, date):
    return f'SELECT * FROM {table} WHERE load_date = "{date}"'

# Execution check: Success