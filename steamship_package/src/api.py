# filename: api.py
# description: This module provides a way to initialize the Memory object with the Steamship API key.

from utils.memory import Memory

api_key = "your_steamship_api_key"
memory = Memory(api_key=api_key)
