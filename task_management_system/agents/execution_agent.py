# filename: execution_agent.py
# description: Defines the ExecutionAgent class, which executes tasks based on roles and interacts with memory.

from utils.memory import Memory
from api import memory
from services.steamship_integration import gpt4_execution_agent, gpt3_5_agent_1, gpt3_5_agent_2, gpt3_5_agent_3

# Dictionary to map roles to their corresponding function
role_to_function_map = {
    "gpt4_execution_agent": gpt4_execution_agent,
    "gpt3_5_agent_1": gpt3_5_agent_1,
    # Add other role-function mappings here
}

class ExecutionAgent:
    def __init__(self):
        self.memory = Memory()

    def execute_task(self, task_id, task_type, role):
        # Retrieve the task from memory
        task, context, priority, role = self.memory.retrieve(task_id)

        # Get the function to execute based on the role
        function_to_execute = self.get_function_to_execute(role, task_type)

        # Execute the function and store the result in memory
        try:
            result = function_to_execute(task, context)
            self.memory.store(task=task, result=result, priority=priority, role=role)
        except Exception as e:
            print(f"An error occurred while executing the task with role '{role}' and type '{task_type}': {e}")

    def get_function_to_execute(self, role, task_type):
        if role == "gpt4":
            if task_type == "execution":
                return gpt4_execution_agent
            else:
                print(f"No function found for task type '{task_type}' and role '{role}'")
        elif role == "gpt3_5":
            if task_type == "execution":
                return gpt3_5_agent_1
            else:
                print(f"No function found for task type '{task_type}' and role '{role}'")
        else:
            print(f"No function found for role '{role}' and task type '{task_type}'")


