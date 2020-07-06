from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import date


class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    is_active: bool = True
    is_superuser: bool = False
    create_time: date = None
    dis_active_time: date = None


class UserCreate(UserBase):
    email = EmailStr
    password = Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str

