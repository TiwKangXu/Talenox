from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.work_arrangements.assignments.models import (
    EmployeeWorkArrangement
)

from app.work_arrangements.assignments.schemas import (
    EmployeeWorkArrangementCreate,
    EmployeeWorkArrangementResponse
)

router = APIRouter(
    prefix="/employee-work-arrangements",
    tags=["Employee Work Arrangements"]
)


@router.post(
    "/",
    response_model=EmployeeWorkArrangementResponse
)
def assign_work_arrangement(
    assignment: EmployeeWorkArrangementCreate,
    db: Session = Depends(get_db)
):

    # Find existing active arrangement
    existing_arrangement = (
        db.query(EmployeeWorkArrangement)
        .filter(
            EmployeeWorkArrangement.employee_id
            == assignment.employee_id,

            EmployeeWorkArrangement.effective_end_date
            == None
        )
        .first()
    )

    # Auto-close previous arrangement
    if existing_arrangement:

        if (
            assignment.effective_start_date
            <= existing_arrangement.effective_start_date
        ):
            raise HTTPException(
                status_code=400,
                detail=(
                    "New arrangement start date "
                    "must be after current arrangement."
                )
            )

        existing_arrangement.effective_end_date = (
            assignment.effective_start_date
            - timedelta(days=1)
        )

    new_assignment = EmployeeWorkArrangement(
        employee_id=assignment.employee_id,
        template_id=assignment.template_id,
        effective_start_date=(
            assignment.effective_start_date
        )
    )

    db.add(new_assignment)

    db.commit()

    db.refresh(new_assignment)

    return new_assignment


@router.get("/")
def get_assignments(
    db: Session = Depends(get_db)
):
    return db.query(
        EmployeeWorkArrangement
    ).all()