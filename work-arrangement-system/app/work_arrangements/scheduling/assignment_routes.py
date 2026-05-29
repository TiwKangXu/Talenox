from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database import get_db

from app.work_arrangements.scheduling.assignment_models import (
    ShiftAssignment
)

from app.work_arrangements.scheduling.assignment_schemas import (
    ShiftAssignmentCreate,
    ShiftAssignmentResponse
)

router = APIRouter(
    prefix="/shift-assignments",
    tags=["Shift Assignments"]
)


@router.post(
    "/",
    response_model=ShiftAssignmentResponse
)
def assign_shift(
    assignment: ShiftAssignmentCreate,
    db: Session = Depends(get_db)
):
    db_assignment = ShiftAssignment(
        employee_id=assignment.employee_id,
        shift_definition_id=assignment.shift_definition_id,
        work_date=assignment.work_date
    )

    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)

    return db_assignment


@router.get("/")
def get_shift_assignments(
    db: Session = Depends(get_db)
):
    return db.query(
        ShiftAssignment
    ).all()