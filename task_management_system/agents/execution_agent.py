# filename: execution_agent.py
# description: Defines the ExecutionAgent class, which executes tasks based on roles and interacts with memory.

from utils.memory import Memory
from api import memory
from services.steamship_integration import (
    gpt4_execution_agent,
    gpt4_task_creation_agent,
    gpt4_task_prioritization_agent,
    gpt4_quality_assurance_agent,
    gpt3_5_software_engineer,
    gpt3_5_cybersecurity_specialist,
)

# Dictionary to map roles to their corresponding function
role_to_function_map = {
    "execution_agent": gpt4_execution_agent,
    "task_creation_agent": gpt4_task_creation_agent,
    "task_prioritization_agent": gpt4_task_prioritization_agent,
    "quality_assurance_agent": gpt4_quality_assurance_agent,
    "software_engineer": gpt3_5_software_engineer,
    "cybersecurity_specialist": gpt3_5_cybersecurity_specialist,
}

class ExecutionAgent:
    def __init__(self):
        self.memory = Memory()

    def execute_task(self, task_id, task_type, role):
        # Retrieve the task from memory
        task, context, priority, role = self.memory.retrieve(task_id)

                # Get the function to execute based on the role
        function_to_execute = self.get_function_to_execute(role)

        # Execute the function and store the result in memory
        try:
            result = function_to_execute(task, context)
            self.memory.store(task=task, result=result, priority=priority, role=role)
            # Remove the executed task from the task list
            self.memory.delete(task_id)
        except Exception as e:
            print(f"An error occurred while executing the task with role '{role}': {e}")

    def get_function_to_execute(self, role):
        function_to_execute = role_to_function_map.get(role)
        if function_to_execute:
            return function_to_execute
        else:
            print(f"No function found for role '{role}'")
            return None

