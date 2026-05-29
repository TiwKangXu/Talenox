from datetime import date

from pydantic import BaseModel


class ShiftAssignmentCreate(
    BaseModel
):
    employee_id: int
    shift_definition_id: int
    work_date: date


class ShiftAssignmentResponse(
    ShiftAssignmentCreate
):
    id: int

    class Config:
        from_attributes = True