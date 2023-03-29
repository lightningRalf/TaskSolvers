# steamship_integration.py
# Description: This module integrates Steamship API with the task management system

from steamship import Steamship

# Replace these values with your actual Steamship API key and GPT-4 package name
STEAMSHIP_API_KEY = "your_steamship_api_key"
GPT4_PACKAGE_NAME = "your_deployed_gpt4_package_name"

# Initialize the Steamship client and create a GPT-4 instance
client = Steamship(api_key=STEAMSHIP_API_KEY)
gpt4_instance = client.package(GPT4_PACKAGE_NAME).create()

def gpt4_generate_text(input_text):
    """
    Generates text using GPT-4 through Steamship.

    Args:
        input_text (str): The input text to generate text based on.

    Returns:
        str: The generated text.
    """
    response = gpt4_instance.post("generate_text", input_text=input_text)
    generated_text = response["result"]
    return generated_text
