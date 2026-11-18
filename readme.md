research-workflow-engine/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── models.py               # Task domain models
│   ├── schemas.py              # Pydantic request validation
│   ├── repository.py           # In-memory task repository
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py     # Task creation and business logic
│   │
│   ├── workers/
│   │   ├── __init__.py
│   │   └── task_worker.py      # Background task execution
│   │
│   └── agents/
│       ├── __init__.py
│       ├── research_agent.py   # Read-only AI agent
│       └── tools.py            # Read-only agent tools
│
├── tests/
│   ├── __init__.py
│   ├── test_repository.py      # Repository unit tests
│   ├── test_tasks.py           # FastAPI endpoint tests
│   ├── test_task_service.py    # Service layer tests
│   └── test_agent.py           # Agent tests
│
├── migrations/                 # Future PostgreSQL migrations
│
├── .env.example                # Environment variable template
├── .gitignore
├── pyproject.toml              # Dependencies and tooling
├── Dockerfile                  # Container configuration
├── docker-compose.yml          # App, database, and worker
└── README.md                   # Setup and architecture