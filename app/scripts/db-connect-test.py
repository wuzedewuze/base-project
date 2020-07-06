import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 间隔1s，重试60*5次
max_tries = 60 * 5
wait_seconds = 1

@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("初始化服务开始")
    init()
    logger.info("初始化服务结束")


if __name__ == '__main__':
    main()
