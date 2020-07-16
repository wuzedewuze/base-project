from pydantic import BaseConfig
import secrets


class Settings(BaseConfig):
    API_V1_STR: str = "/api/v1"
    # token 保存的时间
    ACCESS_TOKEN_EXPIRE_MINUTES: int =60 * 24 * 8
    # token 生成的密钥
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # 数据库配置
    MYSQL_SERVER: str = "192.168.101.130:3401"
    MYSQL_USER: str = "wuyang"
    MYSQL_PASSWORD: str = "274595861"
    MYSQL_DB: str = "wuyang"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}?charset=utf8"

    # 初始化的超级管理员账号秘密
    FIRST_SUPERUSER: str = "wuyang"
    FIRST_SUPERUSER_PASSWORD: str = "wuyang123"

    # 设置区分大小写
    class Config:
        case_sensitive = True


settings = Settings()
