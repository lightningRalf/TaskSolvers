# filename: execution_agent.py
# description: Processes tasks based on roles and interacts with memory.

from utils.memory import Memory

# Dictionary to map roles to their corresponding function
role_to_function_map = {
    "gpt4_execution_agent": gpt4_execution_agent,
    "gpt3_5_agent_1": gpt3_5_agent_1,
    # Add other role-function mappings here
}

# Initialize memory
api_key = "your_steamship_api_key"
memory = Memory(api_key=api_key)

while task_queue:
    # ...
    current_task = task_queue.pop(0)  # Retrieve the next task from the queue
    result = None

    # Execute the task based on the type and role
    function_to_execute = role_to_function_map.get(f"{current_task['role']}_{current_task['type']}")

    try:
        if function_to_execute:
            task, context, priority, role = memory.retrieve(current_task["task_id"])
            result = function_to_execute(task, context)
            memory.store(task=task, result=result, priority=priority, role=role)
        else:
            print(f"No function found for role '{current_task['role']}' and type '{current_task['type']}'")
    except Exception as e:
        print(f"An error occurred while executing the task with role '{current_task['role']}' and type '{current_task['type']}': {e}")
        continue

    # Process the result and add new tasks to the queue
    if result:
        print("Task result:", result)
