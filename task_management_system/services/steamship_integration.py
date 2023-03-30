# steamship_integration.py
# Description: This module integrates Steamship API with the task management system

from steamship import Steamship
from api import CustomSteamshipPackage
from config import instances, LLM_model, specific_traits

def create_instance(instance_handle, model_type, custom_parameters):
    instance = Steamship(api_key=steamship_api_key)
    instance.model_type = model_type
    instance.instance_handle = instance_handle
    instance.custom_parameters = custom_parameters
    return instance

instances = {}

# Create LLM instances
for model_type, model_instances in LLM_model.items():
    for instance_handle, instance_config in model_instances.items():
        instance = create_instance(instance_handle, model_type, instance_config)
        instances[instance_handle] = instance


# Access the instances using their handles, e.g.:
execution_agent_instance = instances["gpt4-execution-agent-instance"]
task_creation_agent_instance = instances["gpt4-task-creation-agent-instance"]
task_prioritization_agent_instance = instances["gpt4-task-prioritization-agent-instance"]

gpt3_5_agent_instance_1 = instances["gpt3-5-agent-instance-1"]
gpt3_5_agent_instance_2 = instances["gpt3-5-agent-instance-2"]
gpt3_5_agent_instance_3 = instances["gpt3-5-agent-instance-3"]

# Initialize LangChain OpenAI instances for GPT-4 instances
langchain_openai_gpt4_execution_agent = LangChainOpenAI(client=instances["gpt4-execution-agent-instance"])
langchain_openai_gpt4_task_creation_agent = LangChainOpenAI(client=instances["gpt4-task-creation-agent-instance"])
langchain_openai_gpt4_task_prioritization_agent = LangChainOpenAI(client=instances["gpt4-task-prioritization-agent-instance"])

# Initialize LangChain OpenAI instances for GPT-3.5 instances
langchain_openai_gpt3_5_1 = LangChainOpenAI(client=instances["gpt3-5-agent-instance-1"])
langchain_openai_gpt3_5_2 = LangChainOpenAI(client=instances["gpt3-5-agent-instance-2"])
langchain_openai_gpt3_5_3 = LangChainOpenAI(client=instances["gpt3-5-agent-instance-3"])

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


