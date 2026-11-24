from pydantic import BaseModel, StringConstraints, ConfigDict
from typing import Annotated, Literal
from uuid import UUID
from datetime import datetime

# {
#   "task_type": "process_dataset",
#   "payload": {
#     "dataset_id": "dataset-123",
#     "operation": "validate"
#   }
# }
class ProcessDatasetPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    dataset_id: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    operation: Literal["validate","transform"]
    
class TaskCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    task_type:  Literal["process_dataset"]
    payload: ProcessDatasetPayload

class TaskResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    task_id: UUID
    task_type: str
    status: str
    created_at: datetime
