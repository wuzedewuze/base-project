from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import date


# 用户的公共基础类
class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    is_active: bool = True
    is_superuser: bool = False
    create_time: date = None
    dis_active_time: date = None


# 通过AIP接受的创建属性
class UserCreate(UserBase):
    email = EmailStr
    password = Optional[str] = None


# 通过AIP接受的更新属性
class UserUpdate(UserBase):
    password: Optional[str] = None


# 入库基础类
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:  # 既可以使用对象又可以使用dict
        orm_mode = True


# 通过AIP返回的附加属性
class User(UserInDBBase):
    pass


# 存储到数据库中的附加属性
class UserInDB(UserInDBBase):
    hashed_password: str

