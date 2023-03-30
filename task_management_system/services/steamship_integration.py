from steamship import Steamship
from api import CustomSteamshipPackage
from config import shared_instance_config, specific_traits

steamship_api_key = "your_steamship_api_key"
gpt4_package_name = "your_deployed_gpt4_package_name"
gpt3_5_package_name = "your_deployed_gpt3_5_package_name"

client = Steamship(api_key=steamship_api_key)

def create_gpt4_instance(instance_handle, custom_parameters):
    instance = Steamship.use(gpt4_package_name, instance_handle, config=shared_instance_config)
    instance.update_parameters(parameters=custom_parameters)
    return instance

def create_gpt3_5_instance(instance_handle):
    instance = Steamship.use(gpt3_5_package_name, instance_handle, config=shared_instance_config)
    instance.update_parameters(parameters=custom_parameters)
    return instance

instances = {}
for instance_handle, custom_parameters in specific_traits.items():
    instances[instance_handle] = create_gpt4_instance(instance_handle, custom_parameters)

# Access the instances using their handles, e.g.:
execution_agent_instance = instances["gpt4-execution-agent-instance"]
task_creation_agent_instance = instances["gpt4-task-creation-agent-instance"]
task_prioritization_agent_instance = instances["gpt4-task-prioritization-agent-instance"]

gpt3_5_agent_instance_1 = instance["gpt3-5-agent-instance-1"]
gpt3_5_agent_instance_2 = instance["gpt3-5-agent-instance-2"]
gpt3_5_agent_instance_3 = instance["gpt3-5-agent-instance-3"]

# Initialize LangChain OpenAI instances for GPT-4 instances
langchain_openai_gpt4_execution_agent = LangChainOpenAI(client=instances["execution-agent-instance"])
langchain_openai_gpt4_task_creation_agent = LangChainOpenAI(client=instances["task-creation-agent-instance"])
langchain_openai_gpt4_task_prioritization_agent = LangChainOpenAI(client=instances["task-prioritization-agent-instance"])

# Initialize LangChain OpenAI instances for GPT-3.5 instances
langchain_openai_gpt3_5_1 = LangChainOpenAI(client=instances["gpt3_5_agent_instance_1"])
langchain_openai_gpt3_5_2 = LangChainOpenAI(client=instances["gpt3_5_agent_instance_2"])
langchain_openai_gpt3_5_3 = LangChainOpenAI(client=instances["gpt3_5_agent_instance_3"])



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


