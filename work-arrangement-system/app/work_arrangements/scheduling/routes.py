from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.work_arrangements.scheduling.models import (
    ShiftDefinition
)

from app.work_arrangements.scheduling.schemas import (
    ShiftDefinitionCreate,
    ShiftDefinitionResponse
)

router = APIRouter(
    prefix="/shift-definitions",
    tags=["Shift Definitions"]
)


@router.post(
    "/",
    response_model=ShiftDefinitionResponse
)
def create_shift_definition(
    shift: ShiftDefinitionCreate,
    db: Session = Depends(get_db)
):
    db_shift = ShiftDefinition(
        name=shift.name,
        start_time=shift.start_time,
        end_time=shift.end_time,
        crosses_midnight=shift.crosses_midnight
    )

    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)

    return db_shift


@router.get("/")
def get_shift_definitions(
    db: Session = Depends(get_db)
):
    return db.query(
        ShiftDefinition
    ).all()