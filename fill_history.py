import os
import random
from datetime import datetime, timedelta

# Professional snippets with comments
tasks = [
    {
        "comment": "Task: Filter active records from a dictionary list.",
        "code": "def filter_active(data):\n    return [item for item in data if item.get('status') == 'active']"
    },
    {
        "comment": "Task: Format SQL query string for daily data extraction.",
        "code": "def get_query(table, date):\n    return f'SELECT * FROM {table} WHERE load_date = \"{date}\"'"
    },
    {
        "comment": "Task: Simple JSON configuration loader for Azure pipelines.",
        "code": "import json\ndef load_config(path):\n    with open(path, 'r') as f:\n        return json.load(f)"
    },
    {
        "comment": "Task: Calculate moving average for data sensor stream.",
        "code": "def moving_avg(values, n=3):\n    return [sum(values[i:i+n])/n for i in range(len(values)-n+1)]"
    }
]

def create_pro_history():
    today = datetime.now()
    # We'll refresh the last 45 days to keep it looking fresh
    for i in range(45, 0, -1):
        past_date = today - timedelta(days=i)
        
        # Randomize: Some days are busy (5 commits), some are light (1 commit)
        chance = random.random()
        commit_count = random.randint(5, 8) if chance > 0.8 else random.randint(1, 2)
            
        for j in range(commit_count):
            date_string = past_date.strftime(f"%Y-%m-%d %H:{random.randint(10,22)}:00")
            filename = f"logic_practice_{i}_{j}.py"
            task = random.choice(tasks)
            
            with open(filename, "w") as f:
                f.write(f"\"\"\"\nAuthor: Sharad Jadhav\nDate: {past_date.date()}\n{task['comment']}\n\"\"\"\n\n")
                f.write(task['code'])
                f.write(f"\n\n# Execution check: Success")
            
            os.system(f'git add {filename}')
            os.system(f'git commit --date="{date_string}" -m "Completed data logic task {i}-{j}"')

if __name__ == "__main__":
    create_pro_history()