# config.py
# Description: Stores and characterizes the different LLMs that will be used

LLM_model = {
    "gpt4": {
        "gpt4-execution-agent-instance": {"role": "execution_agent", "traits": "focused", "other_parameter": "custom_value"},
        "gpt4-task-creation-agent-instance": {"role": "task_creation_agent", "traits": "creative", "other_parameter": "custom_value"},
        "gpt4-task-prioritization-agent-instance": {"role": "task_prioritization_agent", "traits": "analytical", "other_parameter": "custom_value"},
       # "gpt4-text-generation-agent-instance": {"role": "text_generation_agent", "traits": "expressive", "other_parameter": "custom_value"},
       # "gpt4-text-analysis-agent-instance": {"role": "text_analysis_agent", "traits": "insightful", "other_parameter": "custom_value"},
    },
    "gpt3_5": {
        "gpt3-5-quality-assurance-engineer-instance": {"role": "lead-quality-assurance-engineer", "traits": "focused", "other_parameter": "custom_value"},
        "gpt3-5-software-engineer-instance": {"role": "software-engineer", "traits": "creative", "other_parameter": "custom_value"},
        "gpt3-5-software-engineer-instance": {"role": "software-engineer", "traits": "creative", "other_parameter": "custom_value"},
        "gpt3-5-cybersecurity-specialist-instance": {"role": "cybersecurity-specialist", "traits": "analytical", "other_parameter": "custom_value"}
    }
}
