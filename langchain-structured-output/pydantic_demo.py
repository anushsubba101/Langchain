from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):

    name: str
    # for default use 
    # name: str = 'anush'
    age: Optional[int] = None
    #emailstr is pydantic buildin datatype
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='a decimal value representing the cgpa of the student')

new_student = {'name':'anush','age':'32','email':'anush111@gmail.com','cgpa':5}

student = Student(**new_student)

print(student)

student_dict = dict(student)
print(student_dict['name','email'])