from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    title: str
    amount: float

class TransactionOut(TransactionCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
