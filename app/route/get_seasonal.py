from __future__ import annotations

from fastapi.responses import ORJSONResponse

from app.settings import SEASONAL_BGS


async def get_seasonal_bgs() -> ORJSONResponse:
    return ORJSONResponse(SEASONAL_BGS)
