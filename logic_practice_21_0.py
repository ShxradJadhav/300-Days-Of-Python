"""
Author: Sharad Jadhav
Date: 2026-02-20
Task: Calculate moving average for data sensor stream.
"""

def moving_avg(values, n=3):
    return [sum(values[i:i+n])/n for i in range(len(values)-n+1)]

# Execution check: Success