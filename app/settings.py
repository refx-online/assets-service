from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def read_list(value: str) -> list[str]:
    return [v.strip() for v in value.split(",")]


def read_bool(value: str) -> bool:
    return value.lower() in ("true", "1", "yes")


def getenv(name: str, default: str | None = None) -> str:
    # NOTE: plain os.environ[name] dies with a bare KeyError at import time,
    # which tells you nothing. fail fast with the actual var name instead.
    value = os.environ.get(name, default)
    if value is None:
        raise RuntimeError(f"missing required env var: {name}")
    return value


DEBUG = read_bool(getenv("DEBUG", "false"))
HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", "9929"))

SEASONAL_BGS = read_list(getenv("SEASONAL_BGS", ""))

MENU_ICON_URL = read_list(getenv("MENU_ICON_URL", ""))
MENU_ONCLICK_URL = getenv("MENU_ONCLICK_URL", "")

EXPIRES_IN = getenv("EXPIRES_IN", "")

ASSETS_DIR = Path(os.environ.get("ASSETS_PATH", ".data/assets"))
AVA_DIR = Path(os.environ.get("AVA_PATH", ".data/avatars"))
