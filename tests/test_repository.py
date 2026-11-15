from datetime import datetime, timezone
from uuid import uuid4

from app.models import Task, TaskType, TaskStatus
from app.taskRepository import TaskRepository
from app.schemas import ProcessDatasetPayload

import pytest

@pytest.fixture
def sample_task() -> Task:
    return Task(
        task_id=uuid4(),
        task_type=TaskType.PROCESS_DATASET,
        payload=ProcessDatasetPayload(
            dataset_id="ds-123",
            operation="validate",
        ),
        status=TaskStatus.PENDING,
        created_at=datetime.now(timezone.utc),
    )
    
def test_save_and_get_task(sample_task: Task):
    repository = TaskRepository()
    repository.save_task(sample_task)
    retrieved = repository.get_task(sample_task.task_id)
    assert retrieved is not None
    assert retrieved.task_id == sample_task.task_id
    assert retrieved.task_type == sample_task.task_type
    assert retrieved.payload == sample_task.payload
    assert retrieved.status == sample_task.status
    assert retrieved.created_at == sample_task.created_at
    assert retrieved is not sample_task
    assert retrieved.payload is not sample_task.payload

def test_get_task_returns_independent_copy(sample_task: Task):
    repository = TaskRepository()
    repository.save_task(sample_task)
    retrieved = repository.get_task(sample_task.task_id)
    assert retrieved is not None
    retrieved.payload.dataset_id = "ds-456"
    retrieved_again = repository.get_task(sample_task.task_id)
    assert retrieved_again is not None
    assert retrieved_again.payload.dataset_id == "ds-123"


