import logging
from fastapi import FastAPI
from app.core.logging import setup_logging
from contextlib import asynccontextmanager
from app.db.session import engine
from sqlalchemy import text

setup_logging()

logger=logging.getLogger(__name__)
@asynccontextmanager
async def lifespan(app:FastAPI):
    logger.info("URL's Application Starts !")
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connection established")
    except Exception:
        logger.exception("Database connection not established")
        raise
    yield

    logger.info("Shutting down the application")
    engine.dispose()


app=FastAPI(
    title="url-shortener",
    version="0.1.0",
    lifespan=lifespan,uv run alembic init alembic
)

logger.info("url_shortener is started")