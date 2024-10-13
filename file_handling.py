import json
from task import Task

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []
