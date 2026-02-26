"""
Author: Sharad Jadhav
Category: Data Transformation
Task: Filter active records for ETL.
"""

def etl_filter(data):
    return [d for d in data if d['active']]