# filename: execution_agent.py
# description: Processes tasks based on roles and interacts with memory.

from utils.memory import Memory
from api import memory


# Dictionary to map roles to their corresponding function
role_to_function_map = {
    "gpt4_execution_agent": gpt4_execution_agent,
    "gpt3_5_agent_1": gpt3_5_agent_1,
    # Add other role-function mappings here
}
