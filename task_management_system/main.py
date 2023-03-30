# main.py
# Description: This script serves as the entry point for the task management system.

from execution_agent.execution_agent import ExecutionAgent
from task_creation_agent.task_creation_agent import TaskCreationAgent
from task_prioritization_agent.task_prioritization_agent import TaskPrioritizationAgent
from services.steamship_integration import task_queue, add_tasks_to_queue

def main():
    # Initialize the agents and other components
    execution_agent = ExecutionAgent()
    task_creation_agent = TaskCreationAgent()
    task_prioritization_agent = TaskPrioritizationAgent()

    # Add the initial objective and its first task to the task queue
    initial_task = {
        "task": "Your initial task",
        "type": "execution",
        "role": "gpt4",  # The assigned role (e.g., gpt4, gpt3_5)
        "priority": 1  # Priority, with lower numbers indicating higher priority
    }
    task_queue.append(initial_task)

    # Implement the main loop of the task management process
    while task_queue:
        current_task = task_queue.pop(0)  # Retrieve the next task from the queue
        result = None

        # Execute the task based on the type and role
        function_to_execute = execution_agent.role_to_function_map.get(f"{current_task['role']}_{current_task['type']}")

        try:
            if function_to_execute:
                task, context, priority, role = execution_agent.memory.retrieve(current_task["task_id"])
                result = function_to_execute(task, context)
                execution_agent.memory.store(task=task, result=result, priority=priority, role=role)
            else:
                print(f"No function found for role '{current_task['role']}' and type '{current_task['type']}'")
        except Exception as e:
            print(f"An error occurred while executing the task with role '{current_task['role']}' and type '{current_task['type']}': {e}")
            continue

        # Process the result and add new tasks to the queue
        if result:
            print("Task result:", result)
            new_tasks = task_creation_agent.generate_new_tasks(result, current_task['task_id'])
            add_tasks_to_queue(new_tasks)

        # Prioritize tasks in the queue
        task_prioritization_agent.prioritize_tasks(task_queue)

if __name__ == "__main__":
    main()
