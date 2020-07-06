import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

if TYPE_CHECKING:
    pass


class Rolse(Base):
    id = Column(Integer, primary_key=True, index=True)
    rolse_name = Column(String(100), unique=True)
