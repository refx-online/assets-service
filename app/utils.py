from __future__ import annotations

from pathlib import Path

from app.state.services import http_client


async def download_achievement_images(assets: Path) -> bool:
    """Download all used achievement images from osu!."""
    achs: list[str] = []

    for resolution in ("", "@2x"):
        for mode in ("osu", "taiko", "fruits", "mania"):
            max_stars = 10 if mode == "osu" else 8
            for star_rating in range(1, max_stars + 1):
                achs.append(f"{mode}-skill-pass-{star_rating}{resolution}.png")
                achs.append(f"{mode}-skill-fc-{star_rating}{resolution}.png")

        for combo in (500, 750, 1000, 2000):
            achs.append(f"osu-combo-{combo}{resolution}.png")

        for mod in (
            "suddendeath",
            "hidden",
            "perfect",
            "hardrock",
            "doubletime",
            "flashlight",
            "easy",
            "nofail",
            "nightcore",
            "halftime",
            "spunout",
        ):
            achs.append(f"all-intro-{mod}{resolution}.png")

    success_count = 0

    for ach in achs:
        r = await http_client.get(
            f"https://assets.ppy.sh/medals/client/{ach}",
            timeout=10.0,
        )

        if r.status_code == 200:
            (assets / ach).write_bytes(r.content)
            success_count += 1

    return success_count == len(achs)
