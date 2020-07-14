from pydantic import BaseConfig


class Settings(BaseConfig):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "wyProject"
    # 数据库配置
    MYSQL_SERVER: str = "192.168.101.130:3401"
    MYSQL_USER: str = "wuyang"
    MYSQL_PASSWORD: str = "274595861"
    MYSQL_DB: str = "wuyang"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}?charset=utf8"

    # 设置区分大小写
    class Config:
        case_sensitive = True


settings = Settings()
