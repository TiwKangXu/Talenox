from datetime import time

from pydantic import BaseModel


class ShiftDefinitionCreate(BaseModel):
    name: str
    start_time: time
    end_time: time
    crosses_midnight: bool = False


class ShiftDefinitionResponse(
    ShiftDefinitionCreate
):
    id: int

    class Config:
        from_attributes = True