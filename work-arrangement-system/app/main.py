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

from app.employees.routes import router as employee_router

from app.work_arrangements.templates.routes import (
    router as template_router
)

app = FastAPI(
    title="Work Arrangement System"
)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(employee_router)


@app.get("/")
def root():
    return {
        "message": "Work Arrangement System Running"
    }