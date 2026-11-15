

from pydantic import BaseModel
from pydantic import ConfigDict
from enum import Enum
from uuid import UUID
from datetime import datetime
from app.schemas import ProcessDatasetPayload
from zoneinfo import ZoneInfo

central_tz=ZoneInfo("America/Chicago")

class TaskStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    
class TaskType(str, Enum):
    PROCESS_DATASET = "process_dataset"
    
class Task(BaseModel):
    model_config = ConfigDict(extra="forbid")
    task_id: UUID
    task_type: TaskType
    payload: ProcessDatasetPayload
    status: TaskStatus
    created_at: datetime = datetime.now(central_tz)