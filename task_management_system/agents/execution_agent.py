# filename: execution_agent.py
# description: Processes tasks based on roles and interacts with memory.

from services.pinecone_integration import memory

# Dictionary to map roles to their corresponding function
role_to_function_map = {
    "gpt4_execution_agent": gpt4_execution_agent,
    "gpt3_5_agent_1": gpt3_5_agent_1,
    # Add other role-function mappings here
}

# Initialize memory
memory = Memory()

while task_queue:
    # ...
    current_task = task_queue.pop(0)  # Retrieve the next task from the queue
    result = None

    # Execute the task based on the type and role
    function_to_execute = role_to_function_map.get(f"{current_task['role']}_{current_task['type']}")

    try:
        if function_to_execute:
            context = memory.get_context(current_task["task"])
            result = function_to_execute(current_task["task"], context)
            memory.store(task=current_task["task"], result=result, priority=current_task["priority"], role=current_task["role"])
        else:
            print(f"No function found for role '{current_task['role']}' and type '{current_task['type']}'")
    except Exception as e:
        print(f"An error occurred while executing the task with role '{current_task['role']}' and type '{current_task['type']}': {e}")
        continue

    # Process the result and add new tasks to the queue
    if result:
        print("Task result:", result)
