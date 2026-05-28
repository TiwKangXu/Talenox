from sqlalchemy import Column, Integer, String

from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    employment_type = Column(
        String,
        nullable=False
    )

    timezone = Column(
        String,
        default="UTC"
    )

    status = Column(
        String,
        default="ACTIVE"
    )