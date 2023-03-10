from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class BaseComplaint(BaseModel):
    title: str
    description: str
    amount: float
