from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.employees.models import Employee
from app.employees.schemas import (
    EmployeeCreate,
    EmployeeResponse
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/", response_model=EmployeeResponse)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    db_employee = Employee(
        name=employee.name,
        employment_type=employee.employment_type,
        timezone=employee.timezone
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


@router.get("/")
def get_employees(
    db: Session = Depends(get_db)
):
    return db.query(Employee).all()