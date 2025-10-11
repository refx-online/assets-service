from __future__ import annotations

from fastapi import Response
from fastapi.responses import FileResponse

from app.settings import ASSETS_DIR


async def get_medal(medal: str) -> FileResponse:
    """Im just not gonna use nginx"""
    file = ASSETS_DIR / medal

    if file.exists() and file.is_file():
        return FileResponse(file)

    return Response(status_code=404)
