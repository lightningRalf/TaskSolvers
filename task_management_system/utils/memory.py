# filename: memory.py
# description: A simple memory class to store and retrieve task/result pairs.

class Memory:
    def __init__(self):
        self._memory_store = {}

    def store(self, task, result):
        """Store a task/result pair in memory."""
        task_id = task["task_id"]
        self._memory_store[task_id] = {"task": task, "result": result}

    def retrieve(self, task_id):
        """Retrieve the task/result pair for a given task_id."""
        task_result_pair = self._memory_store.get(task_id)
        if task_result_pair:
            return task_result_pair["task"], task_result_pair["result"]
        return None, None

    def get_all_tasks(self):
        """Retrieve all tasks stored in memory."""
        return [task_result_pair["task"] for task_result_pair in self._memory_store.values()]

    def get_all_results(self):
        """Retrieve all results stored in memory."""
        return [task_result_pair["result"] for task_result_pair in self._memory_store.values()]
