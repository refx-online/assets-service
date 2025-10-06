from __future__ import annotations

from fastapi import APIRouter
from fastapi import Response
from fastapi.responses import FileResponse
from fastapi.responses import ORJSONResponse

from app.settings import ASSETS_DIR
from app.settings import EXPIRES_IN
from app.settings import MENU_ICON_URL
from app.settings import MENU_ONCLICK_URL
from app.settings import SEASONAL_BGS

router = APIRouter(tags=["Assets"])


@router.get("/menu-content.json")
def get_menu_content():
    return ORJSONResponse(
        content={
            "images": [
                {
                    "image": MENU_ICON_URL,
                    "url": MENU_ONCLICK_URL,
                    "IsCurrent": True,  # ??
                    "begins": None,  # ??
                    "expires": EXPIRES_IN,
                },
            ],
        },
    )


@router.get("/web/osu-getseasonal.php")
async def get_seasonal() -> Response:
    return ORJSONResponse(SEASONAL_BGS)


@router.get("/health")
def health():
    return ORJSONResponse(
        # Yes
        content={
            "ok": True,
        },
    )


@router.get("/medals/client/{medal}")
async def get_medal(medal: str):
    """Im just not gonna use nginx"""
    file = ASSETS_DIR / medal

    if file.exists() and file.is_file():
        return FileResponse(file)

    return Response(status_code=404)
