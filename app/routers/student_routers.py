from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.students_model import Student
from app.schemas.student_schema import StudentCreate, StudentShow

router = APIRouter()

# Insert new student
@router.post("/students/", response_model=StudentShow)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        name=student.name,
        rollnumber=student.rollnumber,
        sec=student.sec
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student