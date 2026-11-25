
from time import strptime
from urllib import response

from fastapi.testclient import TestClient
from uuid import UUID
from app.main import app
from app.models import TaskStatus, TaskType
import datetime as dt


client = TestClient(app)


def test_create_task_returns_201():
    response = client.post(
        "/tasks",
        json={
            "task_type": "process_dataset",
            "payload": {
                "dataset_id": "ds-123",
                "operation": "validate"
            }
        }
    )
    data = response.json()
    # Add your assertions here.
    assert response.status_code == 201
    assert isinstance(UUID(data["task_id"]), UUID)
    assert data["status"] == TaskStatus.PENDING.value
    assert data["task_type"] == TaskType.PROCESS_DATASET.value
    assert "created_at" in data
    assert data["created_at"] is not None
    created_at = dt.datetime.fromisoformat(data["created_at"])
    assert created_at.utcoffset() == dt.timedelta(0)
   