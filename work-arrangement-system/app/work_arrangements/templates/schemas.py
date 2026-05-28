from pydantic import BaseModel
from typing import Dict, Any


class WorkArrangementTemplateCreate(BaseModel):
    name: str
    arrangement_type: str
    rules: Dict[str, Any]


class WorkArrangementTemplateResponse(
    WorkArrangementTemplateCreate
):
    id: int

    class Config:
        from_attributes = True