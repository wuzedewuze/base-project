from fastapi import FastAPI
from app.core.config import Settings

app = FastAPI(title=Settings.PROJECT_NAME, openapi_url=f"{Settings.API_V1_STR}/openapi.json")
