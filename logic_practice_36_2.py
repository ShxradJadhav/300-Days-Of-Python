"""
Author: Sharad Jadhav
Date: 2026-02-05
Task: Simple JSON configuration loader for Azure pipelines.
"""

import json
def load_config(path):
    with open(path, 'r') as f:
        return json.load(f)

# Execution check: Success