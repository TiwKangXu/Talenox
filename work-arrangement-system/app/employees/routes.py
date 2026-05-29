from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.employees.models import Employee
from app.employees.schemas import (
    EmployeeCreate,
    EmployeeResponse
)

from datetime import date
from fastapi import Query
from app.work_arrangements.scheduling.assignment_models import (
    ShiftAssignment
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

@router.get("/{employee_id}/is-working-day")
def is_working_day(
    employee_id: int,
    target_date: date = Query(...),
    db: Session = Depends(get_db)
):
    shift_assignment = (
        db.query(ShiftAssignment)
        .filter(
            ShiftAssignment.employee_id == employee_id,
            ShiftAssignment.work_date == target_date
        )
        .first()
    )

    return {
        "employee_id": employee_id,
        "date": target_date,
        "is_working_day": shift_assignment is not None
    }