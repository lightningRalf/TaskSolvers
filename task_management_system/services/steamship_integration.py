from steamship import Steamship
from api import CustomSteamshipPackage

steamship_api_key = "your_steamship_api_key"
gpt4_package_name = "your_deployed_gpt4_package_name"

client = Steamship(api_key=steamship_api_key)

def create_gpt4_instance(custom_parameters, instance_handle):
    instance = Steamship.use(gpt4_package_name, instance_handle, config=custom_parameters)
    return instance

# Customize the instances based on their specific roles
shared_instance_handle = "shared-instance-handle"
shared_instance_config = {"traits": "balanced"}

execution_agent_instance = create_gpt4_instance(shared_instance_config, shared_instance_handle)
task_creation_agent_instance = create_gpt4_instance(shared_instance_config, shared_instance_handle)
task_prioritization_agent_instance = create_gpt4_instance(shared_instance_config, shared_instance_handle)

def gpt4_execution_agent(input_text):
    response = execution_agent_instance.post("execute_task", input_text=input_text)
    result = response["result"]
    return result

def gpt4_task_creation_agent(input_text):
    response = task_creation_agent_instance.post("create_tasks", input_text=input_text)
    new_tasks = response["result"]
    return new_tasks

def gpt4_task_prioritization_agent(input_text):
    response = task_prioritization_agent_instance.post("prioritize_tasks", input_text=input_text)
    prioritized_tasks = response["result"]
    return prioritized_tasks
