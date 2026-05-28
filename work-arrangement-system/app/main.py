from fastapi import FastAPI

from app.database import Base, engine

# Import models
from app.employees.models import Employee

from app.work_arrangements.templates.models import (
    WorkArrangementTemplate
)

from app.work_arrangements.assignments.models import (
    EmployeeWorkArrangement
)

app = FastAPI(
    title="Work Arrangement System"
)

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Work Arrangement System Running"
    }