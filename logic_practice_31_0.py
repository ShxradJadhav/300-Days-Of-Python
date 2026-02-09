"""
Author: Sharad Jadhav
Date: 2026-02-10
Task: Filter active records from a dictionary list.
"""

def filter_active(data):
    return [item for item in data if item.get('status') == 'active']

# Execution check: Success