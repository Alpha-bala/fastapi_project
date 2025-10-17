from fastapi import FastAPI
from app.database import engine, Base

from app.routers import student_routers

from app.models.students_model import Student


app=FastAPI()


# Create all tables in the database
Base.metadata.create_all(bind=engine)
app.include_router(student_routers.router)