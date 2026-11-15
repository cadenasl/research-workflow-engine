from datetime import datetime, timezone

from app.models import Task, TaskType, TaskStatus
from app.taskRepository import TaskRepository
from app.schemas import ProcessDatasetPayload
from uuid import uuid4

def test_save_and_get_task():
    repository = TaskRepository()

    task = Task(
        task_id=uuid4(),
        task_type=TaskType.PROCESS_DATASET,
        payload=ProcessDatasetPayload(
            dataset_id="ds-123",
            operation="validate",
        ),
        status=TaskStatus.PENDING,
        created_at=datetime.now(timezone.utc),
    )

    repository.save_task(task)
    retrieved = repository.get_task(task.task_id)
    assert retrieved is not None
    assert retrieved.task_id == task.task_id
    assert retrieved.task_type == task.task_type
    assert retrieved.payload == task.payload
    assert retrieved.status == task.status
    assert retrieved.created_at == task.created_at


