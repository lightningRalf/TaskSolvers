# filename: memory.py
# description: This module provides a Memory class to store and retrieve task/result pairs using the Steamship API.

import json
from api import api_key

class Memory:
    def __init__(self):
        self.steamship = Steamship(api_key=api_key)

    def store(self, task, result, priority, role):
        """Store a task/result pair with priority and role in memory."""
        task_id = task["task_id"]
        task_data = {
            "task": task,
            "result": result,
            "priority": priority,
            "role": role
        }
        self.steamship.set(task_id, json.dumps(task_data))

    def retrieve(self, task_id):
        """Retrieve the task/result pair with priority and role for a given task_id."""
        task_data_str = self.steamship.get(task_id)
        if task_data_str:
            task_data = json.loads(task_data_str)
            return task_data["task"], task_data["result"], task_data["priority"], task_data["role"]
        return None, None, None, None

    def delete(self, task_id):
        """Delete a task/result pair with priority and role for a given task_id."""
        self.steamship.delete(task_id)

