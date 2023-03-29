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
project_root/
├── steamship_package/
│   ├── src/
│   │   └── api.py          # done in first iteration
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_api.py
│   ├── .gitignore
│   ├── README.md
│   ├── requirements.txt
│   ├── requirements.dev.txt
│   └── steamship.yml
├── task_management_system/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── execution_agent.py  # done in first
│   │   ├── task_creation_agent.py
│   │   └── task_prioritization_agent.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── steamship_integration.py    # done in first
│   │   ├── pinecone_integration.py
│   │   └── langchain_integration.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── memory.py
│   │   └── queue.py
│   └── main.py
├── .gitignore
└── README.md
