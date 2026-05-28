from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship

from app.database import Base


class EmployeeWorkArrangement(Base):
    __tablename__ = "employee_work_arrangements"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    template_id = Column(
        Integer,
        ForeignKey("work_arrangement_templates.id"),
        nullable=False
    )

    effective_start_date = Column(
        DateTime,
        nullable=False
    )

    effective_end_date = Column(
        DateTime,
        nullable=True
    )

    employee = relationship("Employee")

    template = relationship(
        "WorkArrangementTemplate"
    )