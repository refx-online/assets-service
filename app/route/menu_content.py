from __future__ import annotations

from fastapi.responses import ORJSONResponse

from app.settings import EXPIRES_IN
from app.settings import MENU_ICON_URL
from app.settings import MENU_ONCLICK_URL


async def get_menu_content() -> ORJSONResponse:
    images = [
        {
            "image": i,
            "url": MENU_ONCLICK_URL,
            "IsCurrent": True,  # ??
            "begins": None,  # ??
            "expires": EXPIRES_IN,
        }
        for i in MENU_ICON_URL
    ]

    return ORJSONResponse(
        content={
            "images": images,
        },
    )
