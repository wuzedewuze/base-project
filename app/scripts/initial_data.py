import logging

from app.db.init_db import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()

    init_db(db)


def main() -> None:
    logger.info("初始化 数据库")
    init()
    logger.info("已完成初始化")


if __name__ == "__main__":
    main()
