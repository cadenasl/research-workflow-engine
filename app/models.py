

from pydantic import BaseModel
from pydantic import ConfigDict
from uuid import UUID
from datetime import datetime
from app.schemas import ProcessDatasetPayload
from zoneinfo import ZoneInfo

central_tz=ZoneInfo("America/Chicago")

class taskStatus(str):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    
class TaskType(str):
    PROCESS_DATASET = "process_dataset"
    
class Task(BaseModel):
    model_config = ConfigDict(extra="forbid")
    task_id: UUID
    task_type: TaskType
    payload: ProcessDatasetPayload
    status: taskStatus
    created_at: datetime = datetime.now(central_tz)