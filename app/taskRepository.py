from uuid import UUID
from app.models import Task
import copy

class TaskRepository:
    def __init__(self):
        self.tasks: dict[UUID, Task] = {}

    def save_task(self, task: Task) -> Task:
        self.tasks[task.task_id] = task.model_copy(deep=True)
        return self.tasks[task.task_id].model_copy(deep=True)

    def get_task(self, task_id: UUID) -> Task | None:
        task = self.tasks.get(task_id)
        return task.model_copy(deep=True) if task is not None else None
    def list_all(self) -> list[Task]:
        return [task.model_copy(deep=True) for task in self.tasks.values()]

   