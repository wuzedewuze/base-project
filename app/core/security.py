from datetime import datetime, timedelta
from typing import  Any, Union

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

# 加密上下文
pwd_context = CryptContext(schemes=["bcrypt"],  deprecated="auto")

# jwt加密设置算法名
ALGORITHM = "HS256"


# 创建token的方法
def create_access_token(
        subject: Any, expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


# 加密方法
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# 验证秘密是否正确
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


















