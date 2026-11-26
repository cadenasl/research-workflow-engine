
from app.taskRepository import TaskRepository
from app.services.task_service import TaskService

_repository = TaskRepository()


def get_task_service() -> TaskService:
    return TaskService(_repository)
