"""
Author: Sharad Jadhav
Category: Math Utilities
Task: Check for outliers in dataset.
"""

def is_outlier(val, avg, std):
    return abs(val - avg) > 2 * std