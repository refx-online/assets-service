from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def read_list(value: str) -> list[str]:
    return [v.strip() for v in value.split(",")]


def read_bool(value: str) -> bool:
    return value.lower() in ("true", "1", "yes")


DEBUG = read_bool(os.environ["DEBUG"])
HOST = os.environ["HOST"]
PORT = int(os.environ["PORT"])

SEASONAL_BGS = read_list(os.environ["SEASONAL_BGS"])

MENU_ICON_URL = read_list(os.environ["MENU_ICON_URL"])
MENU_ONCLICK_URL = os.environ["MENU_ONCLICK_URL"]

EXPIRES_IN = os.environ["EXPIRES_IN"]

ASSETS_DIR = Path.cwd() / ".data/assets"
