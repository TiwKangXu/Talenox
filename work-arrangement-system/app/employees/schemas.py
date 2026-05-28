from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    employment_type: str
    timezone: str = "UTC"


class EmployeeResponse(EmployeeCreate):
    id: int
    status: str

    class Config:
        from_attributes = True