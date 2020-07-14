from typing import Generator, Dict

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.core.config import Settings
from app.db.session import SessionLocal


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def clinet() -> Generator:
    with TestClient(app) as c:
        yield c










