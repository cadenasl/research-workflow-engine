
from app.models import TaskStatus, TaskType
from uuid import UUID
from app.taskRepository import TaskRepository
from app.schemas import TaskCreate, ProcessDatasetPayload
from app.services.task_service import TaskService
from datetime import timedelta


def test_create_task():
    repository = TaskRepository()
    service = TaskService(repository)

    request = TaskCreate(
        task_type="process_dataset",
        payload=ProcessDatasetPayload(
            dataset_id="ds-123",
            operation="validate",
        ),
    )

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
    

