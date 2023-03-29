# TaskSolvers

First, clone the Steamship starter package and set up a virtual environment following the instructions from the Steamship documentation:
```bash copy code
git clone https://github.com/steamship-packages/empty-package.git
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install -r requirements.dev.txt
```

## Folder structure
- project_root/
    - steamship_package/
        - src/
            - api.py
        - tests/
            - __init__.py
            - test_api.py
        - .gitignore
        - README.md
        - requirements.txt
        - requirements.dev.txt
        - steamship.yml
    - task_management_system/
        - execution_agent/
            - __init__.py
            - execution_agent.py
        - task_creation_agent/
            - __init__.py
            - task_creation_agent.py
        - task_prioritization_agent/
            - __init__.py
            - task_prioritization_agent.py
        - utils/
            - __init__.py
            - memory.py
            - queue.py
        - main.py
    - .gitignore
    - README.md
