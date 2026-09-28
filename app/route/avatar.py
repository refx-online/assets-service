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

    # NOTE (local setup): default avatar may be any supported ext,
    # not just jpg.
    for ext in EXTS:
        default = AVA_DIR / f"default.{ext}"
        if default.exists():
            return FileResponse(default)

    return Response(status_code=404)
