from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate


class CRUDUser(CRUDBase[Role, RoleCreate, RoleUpdate]):
    def get