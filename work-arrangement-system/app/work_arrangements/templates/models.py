from sqlalchemy import Column, Integer, String, JSON

from app.database import Base


class WorkArrangementTemplate(Base):
    __tablename__ = "work_arrangement_templates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        nullable=False
    )

    arrangement_type = Column(
        String,
        nullable=False
    )

    # Flexible configuration storage
    rules = Column(
        JSON,
        nullable=False
    )