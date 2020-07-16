from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.core.config import settings

# 固定格式生成数据库引擎
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# 创建连接sessiong
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




