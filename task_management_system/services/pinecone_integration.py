# pinecone_integration.py
# Description: This module integrates Pinecone vector database service with the task management system

from memory import Memory
import os

# Check if Pinecone API key is available in the environment
if "PINECONE_API_KEY" not in os.environ:
    raise ValueError("Pinecone API key is missing. Please set the environment variable 'PINECONE_API_KEY'")

# Initialize Memory class using Pinecone
memory = Memory()

# Sample usage of memory class
# Store task/result pair
# memory.store(task={"task_id": "sample_task"}, result={"result_key": "sample_result"}, priority=1, role="gpt4")

# Retrieve task/result pair
# task, result, priority, role = memory.retrieve(task_id="sample_task")
# print(f"Task: {task}, Result: {result}, Priority: {priority}, Role: {role}")
