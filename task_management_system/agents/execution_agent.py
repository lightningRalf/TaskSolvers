def execute_task(task):
    task_type, task_data = task

    try:
        if task_type == "gpt4_generate_text":
            input_text = task_data
            generated_text = gpt4_generate_text(input_text)
            return generated_text
        else:
            print(f"Unknown task type: {task_type}")
            return None
    except Exception as e:
        print(f"An error occurred while executing the task: {e}")
        return None
