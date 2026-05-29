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

# Import routers
from app.employees.routes import (
    router as employee_router
)

from app.work_arrangements.templates.routes import (
    router as template_router
)

from app.work_arrangements.assignments.routes import (
    router as assignment_router
)

from app.work_arrangements.scheduling.models import (
    ShiftDefinition
)

from app.work_arrangements.scheduling.assignment_models import (
    ShiftAssignment
)

from app.work_arrangements.scheduling.routes import (
    router as shift_definition_router
)

from app.work_arrangements.scheduling.assignment_routes import (
    router as shift_assignment_router
)

app = FastAPI(
    title="Work Arrangement System"
)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(employee_router)
app.include_router(template_router)
app.include_router(assignment_router)
app.include_router(shift_definition_router)
app.include_router(shift_assignment_router)

@app.get("/")
def root():
    return {
        "message": "Work Arrangement System Running"
    }