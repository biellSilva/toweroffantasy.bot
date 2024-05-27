from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator


class Banner(BaseModel):
    simulacrumId: str | None
    weaponId: str | None
    matrixId: str | None
    simulacrumName: str | None
    element: str | None
    category: str | None
    simulacrumIcon: str | None
    weaponIcon: str | None
    rarity: int = 5
    bannerNumber: int
    startDate: Annotated[datetime, BeforeValidator(datetime.fromisoformat)]
    endDate: Annotated[datetime, BeforeValidator(datetime.fromisoformat)]
    detailsLink: str
    isLimitedBannerOnly: bool
    isRerun: bool
    isFinalBanner: bool
    isCollab: bool
    noWeapon: bool
