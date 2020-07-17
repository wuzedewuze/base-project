from typing import Optional

from pydantic import BaseModel


# 用户的公共基础类
class RoleBase(BaseModel):
    rolse_name: str


# 通过AIP接受的创建属性
class RoleCreate(RoleBase):
    pass


# 通过AIP接受的更新属性
class RoleUpdate(RoleBase):
    pass


# 入库基础类
class RoleInDBBase(RoleBase):
    id: int

    class Config:  # 既可以使用对象又可以使用dict
        orm_mode = True


# 通过AIP返回的附加属性
class Role(RoleInDBBase):
    pass


# 存储到数据库中的附加属性
class RoleInDB(RoleInDBBase):
    pass

