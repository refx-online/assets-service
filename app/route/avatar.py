from __future__ import annotations

from fastapi import Response
from fastapi.responses import FileResponse

from app.settings import AVA_DIR

EXTS = ("png", "jpg", "jpeg", "gif")


async def get_avatar(id: int) -> FileResponse | Response:
    for ext in EXTS:
        file = AVA_DIR / f"{id}.{ext}"
        if file.exists():
            return FileResponse(file)

    default = AVA_DIR / "default.jpg"
    if default.exists():
        return FileResponse(default)

    return Response(status_code=404)
