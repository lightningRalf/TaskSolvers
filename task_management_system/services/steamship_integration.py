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

def create_gpt3_5_instance(custom_parameters, instance_handle):
    instance = Steamship.use("your_deployed_gpt3_5_package_name", instance_handle, config=custom_parameters)
    return instance

# Customize the instances based on their specific roles
gpt3_5_instance_handle = "gpt3-5-shared-instance-handle"
gpt3_5_shared_instance_config = {"traits": "balanced"}

gpt3_5_agent_instance_1 = create_gpt3_5_instance(gpt3_5_shared_instance_config, gpt3_5_instance_handle)
gpt3_5_agent_instance_2 = create_gpt3_5_instance(gpt3_5_shared_instance_config, gpt3_5_instance_handle)
gpt3_5_agent_instance_3 = create_gpt3_5_instance(gpt3_5_shared_instance_config, gpt3_5_instance_handle)

def gpt3_5_agent_1(input_text):
    response = gpt3_5_agent_instance_1.post("execute_task", input_text=input_text)
    result = response["result"]
    return result

def gpt3_5_agent_2(input_text):
    response = gpt3_5_agent_instance_2.post("execute_task", input_text=input_text)
    result = response["result"]
    return result

def gpt3_5_agent_3(input_text):
    response = gpt3_5_agent_instance_3.post("execute_task", input_text=input_text)
    result = response["result"]
    return result


