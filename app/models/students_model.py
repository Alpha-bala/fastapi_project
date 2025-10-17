from sqlalchemy import Column, Integer, String
from  app.database import Base # import Base from your database.py





class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    rollnumber = Column(Integer, nullable=False)
    sec = Column(String(10), nullable=False)