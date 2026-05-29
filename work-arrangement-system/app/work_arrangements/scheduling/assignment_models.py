from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Date
)

from sqlalchemy.orm import relationship

from app.database import Base


class ShiftAssignment(Base):
    __tablename__ = "shift_assignments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    shift_definition_id = Column(
        Integer,
        ForeignKey("shift_definitions.id"),
        nullable=False
    )

    work_date = Column(
        Date,
        nullable=False
    )

    employee = relationship(
        "Employee"
    )

    shift = relationship(
        "ShiftDefinition"
    )