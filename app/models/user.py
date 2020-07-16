import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from app.core.config import settings

if TYPE_CHECKING:
    pass


# 多对多表的关联关系中间表
class User2Rolse(Base):
    id = Column(Integer, primary_key=True, index=True)
    rolse_id = Column(Integer, ForeignKey('rolse.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(1000), nullable=False)
    email = Column(String(100), index=True, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    create_time = Column(DateTime, default=datetime.datetime.now)
    dis_active_time = Column(DateTime,
                             default=datetime.datetime.now()+datetime.timedelta(days=settings.USER_ACTIVE_DEFAULT_TIME),
                             nullable=True)
    # 与生成的表结果无关，仅仅用于方便查询， rolse用于正常查询，rolse用于反向查询
    roles = relationship("Rolse",  # 字符串类型的 映射类名称
                         secondary='user2rolse', backref='user')


class Rolse(Base):
    id = Column(Integer, primary_key=True, index=True)
    rolse_name = Column(String(100), unique=True)
