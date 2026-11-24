
from app.models import Task,TaskType, TaskStatus
from app.schemas import TaskCreate
from app.taskRepository import TaskRepository
from uuid import  uuid4
from datetime import datetime, timezone


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def create_task(self, request: TaskCreate) -> Task:
        # 1. Generate a UUID
        task_id = uuid4() 

        # 2. Create a timezone-aware UTC timestamp
        now = datetime.now(timezone.utc)

        # 3. Construct a Task with status PENDING
        task = Task(
            task_id=task_id,
            status=TaskStatus.PENDING,
            task_type=TaskType.PROCESS_DATASET,
            payload=request.payload,
            created_at=now,
            
        )

        # 4. Save it through the repository

        # 5. Return the saved Task
        return self.repository.save_task(task) 
