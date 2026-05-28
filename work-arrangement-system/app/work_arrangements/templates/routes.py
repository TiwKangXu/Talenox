from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.work_arrangements.templates.models import (
    WorkArrangementTemplate
)

from app.work_arrangements.templates.schemas import (
    WorkArrangementTemplateCreate,
    WorkArrangementTemplateResponse
)

router = APIRouter(
    prefix="/work-arrangement-templates",
    tags=["Work Arrangement Templates"]
)


@router.post(
    "/",
    response_model=WorkArrangementTemplateResponse
)
def create_template(
    template: WorkArrangementTemplateCreate,
    db: Session = Depends(get_db)
):
    db_template = WorkArrangementTemplate(
        name=template.name,
        arrangement_type=template.arrangement_type,
        rules=template.rules
    )

    db.add(db_template)
    db.commit()
    db.refresh(db_template)

    return db_template


@router.get("/")
def get_templates(
    db: Session = Depends(get_db)
):
    return db.query(
        WorkArrangementTemplate
    ).all()