from datetime import datetime

from pydantic import BaseModel


class EmployeeWorkArrangementCreate(
    BaseModel
):
    employee_id: int
    template_id: int
    effective_start_date: datetime


class EmployeeWorkArrangementResponse(
    EmployeeWorkArrangementCreate
):
    id: int
    effective_end_date: datetime | None

    class Config:
        from_attributes = True