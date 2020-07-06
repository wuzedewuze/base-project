from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


# 声明modle基础类
@as_declarative()
class Base:
    # 自动添加ID
    id: Any
    __name__: str
    
    # 自动生成表名
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
