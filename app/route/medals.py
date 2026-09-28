from __future__ import annotations

from fastapi import Response
from fastapi.responses import FileResponse

from app.settings import ASSETS_DIR


async def get_medal(medal: str) -> FileResponse:
    """Im just not gonna use nginx"""
    # NOTE: medal comes straight from the URL path. reject separators and
    # parent refs, then verify the resolved path stays inside ASSETS_DIR
    # so ../ can't escape into arbitrary local files.
    if "/" in medal or "\\" in medal or ".." in medal:
        return Response(status_code=404)

    file = (ASSETS_DIR / medal).resolve()
    if not file.is_relative_to(ASSETS_DIR.resolve()):
        return Response(status_code=404)

    if file.exists() and file.is_file():
        return FileResponse(file)

    return Response(status_code=404)
