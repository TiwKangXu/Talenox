from sqlalchemy import (
    Column,
    Integer,
    String,
    Time,
    Boolean
)

from app.database import Base


class ShiftDefinition(Base):
    __tablename__ = "shift_definitions"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        nullable=False
    )

    start_time = Column(
        Time,
        nullable=False
    )

    end_time = Column(
        Time,
        nullable=False
    )

    crosses_midnight = Column(
        Boolean,
        default=False
    )