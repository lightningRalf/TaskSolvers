# TaskSolvers

Based on:
[Yohei's Tweet (@yoheinakamajima)](https://twitter.com/yoheinakajima/status/1640934493489070080?s=46&t=tuKaIlkHjg0xHde1FOd6zQ)
Written completely by GPT-4

To set up the system you described, follow these steps:

Integrate the Steamship API by following the documentation provided on https://docs.steamship.com/. This will enable communication with the Steamship platform.

Integrate Pinecone (a vector database) and Langchain (a language translation API) if necessary, to aid the execution agent (GPT-4) in completing tasks that require these additional tools.

Develop a task management system with the following components:

a. Task Queue: A data structure to store tasks that need to be processed.

b. Execution Agent (GPT-4): Responsible for processing tasks from the task queue.

c. Task Creation Agent (GPT-4): Responsible for generating new tasks based on the results of previous tasks.

d. Task Prioritization Agent (GPT-4): Responsible for prioritizing tasks in the queue and removing duplicates.

Implement the following process:

a. Add the initial objective and its first task to the task queue.

b. The Execution Agent retrieves tasks from the task queue, queries memory for context, solves the task, and stores the task/result pair in memory.

c. Send the task result to the Task Creation Agent, which queries memory for context and generates new tasks (up to a maximum of 3) based on the result. These tasks are added to the task queue.

d. The Task Prioritization Agent retrieves all tasks from the task queue, prioritizes them, removes duplicates, and repopulates the task queue with the cleaned and improved task list.

e. Repeat steps b through d until the initial objective is solved.

This system will iteratively solve tasks, generate new tasks based on results, and prioritize tasks in the queue until the initial objective is completed. Note that some customization may be necessary to integrate GPT-4 with Steamship, Pinecone, and Langchain, as well as for the task management components.



First, clone the Steamship starter package and set up a virtual environment following the instructions from the Steamship documentation:
```bash copy code
git clone https://github.com/steamship-packages/empty-package.git
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install -r requirements.dev.txt
```

## Folder structure

```
project_root/
├── steamship_package/
│   ├── src/
│   │   └── api.py
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
│   │   ├── execution_agent.py
│   │   ├── task_creation_agent.py
│   │   └── task_prioritization_agent.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── steamship_integration.py
│   │   ├── pinecone_integration.py
│   │   └── langchain_integration.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── memory.py
│   │   └── queue.py
│   └── main.py
├── .gitignore
└── README.md
```
