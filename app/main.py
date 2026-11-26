from typing import Annotated

from fastapi import Depends, FastAPI, status
from app.services.task_service import TaskService
from app.schemas import TaskCreate, TaskResponse
from app.taskRepository import TaskRepository
from app.dependencies import get_task_service

app = FastAPI(
    title="Research Workflow Engine",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}

@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    request: TaskCreate,
    service: Annotated[TaskService, Depends(get_task_service)]
) -> TaskResponse:
    # Call the service to create a task
    # Return the saved task
    task = service.create_task(request)
    return TaskResponse(
        task_id=task.task_id,
        task_type=task.task_type.value,
        status=task.status.value,
        created_at=task.created_at
    )