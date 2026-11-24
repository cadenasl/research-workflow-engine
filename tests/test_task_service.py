
from app.models import TaskStatus, TaskType
from uuid import UUID
from app.taskRepository import TaskRepository
from app.schemas import TaskCreate, ProcessDatasetPayload
from app.services.task_service import TaskService
from datetime import timedelta
from unittest.mock import Mock
import pytest

@pytest.fixture
def sample_request() -> TaskCreate:
    return TaskCreate(
        task_type="process_dataset",
        payload=ProcessDatasetPayload(
            dataset_id="ds-123",
            operation="validate",
        ),
    )
def test_create_task(sample_request):
    repository = TaskRepository()
    service = TaskService(repository)

    request = sample_request

    task = service.create_task(request)
    task_retrieved = repository.get_task(task.task_id)

    # Your assertions go here.
    assert isinstance(task.task_id, UUID)
    assert task.status == TaskStatus.PENDING
    assert task.task_type == TaskType.PROCESS_DATASET
    assert task.payload.dataset_id == "ds-123"
    assert task.payload.operation == "validate"
    assert task_retrieved is not None
    assert task_retrieved == task
    assert task.created_at.utcoffset() == timedelta(0)
    

def test_create_task_propagates_repository_error(sample_request):
    repository = Mock(spec=TaskRepository)
    repository.save_task.side_effect = RuntimeError(
        "Database unavailable"
    )

    service = TaskService(repository)

    # 1. Create a valid TaskCreate request.
    
    request = sample_request
    # 2. Call service.create_task() inside
    #    pytest.raises(RuntimeError).
    with pytest.raises(RuntimeError, match="Database unavailable"):
        service.create_task(request)
    # 3. Verify repository.save_task was called once
    repository.save_task.assert_called_once()
    

