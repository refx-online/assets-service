from __future__ import annotations

from fastapi import APIRouter
from fastapi import Response

from . import get_seasonal
from . import medals
from . import menu_content

router = APIRouter(default_response_class=Response, tags=["Assets"])

router.add_api_route("/menu-content.json", menu_content.get_menu_content)

router.add_api_route("/web/osu-getseasonal.php", get_seasonal.get_seasonal_bgs)

router.add_api_route("/medals/client/{medal}", medals.get_medal)

# TODO: will be used for storing replays in the future if possible
