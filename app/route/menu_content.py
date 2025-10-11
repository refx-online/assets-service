from __future__ import annotations

from fastapi.responses import ORJSONResponse

from app.settings import EXPIRES_IN
from app.settings import MENU_ICON_URL
from app.settings import MENU_ONCLICK_URL


def get_menu_content() -> ORJSONResponse:
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
