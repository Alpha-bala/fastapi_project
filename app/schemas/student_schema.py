from pydantic import BaseModel

# Common fields
class StudentBase(BaseModel):
    name: str
    rollnumber: int
    sec: str

# For creating student (input)
class StudentCreate(StudentBase):
    pass

# For showing student (output)
class StudentShow(StudentBase):
    id: int


    class Config:
        from_attributes = True