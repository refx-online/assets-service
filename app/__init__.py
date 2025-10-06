from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from app.route import router as route_router
from app.settings import ASSETS_DIR
from app.state.services import http_client
from app.utils import download_achievement_images


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not ASSETS_DIR.exists():
        ASSETS_DIR.mkdir(parents=True)
        await download_achievement_images(ASSETS_DIR)

    yield

    await http_client.aclose()


asgi_app = FastAPI(
    title="assets-service",
    lifespan=lifespan,
)

asgi_app.include_router(route_router)
