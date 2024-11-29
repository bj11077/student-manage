from pydantic import BaseModel
from typing import List,Any

class Student(BaseModel):
    manageId: str
    name : str
    expiredDate : str
    absenceCount: int


class ResponseForm(BaseModel):
    data: Any