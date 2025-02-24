import re
from enum import Enum, StrEnum
from typing import Annotated

from discord import PartialEmoji
from pydantic import AfterValidator

__all__ = (
    "LangsEnum",
    "RarityEnum",
    "QualityEnum",
    "EmojisEnum",
    "ParseRegex",
    "ElementEnum",
    "CategoryEnum",
)


class LangsEnum(StrEnum):
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    ID = "id"
    JA = "ja"
    PT = "pt"
    RU = "ru"
    TH = "th"
    ZH_CN = "zh-CN"


class RarityEnum(StrEnum):
    N = "N"
    R = "R"
    SR = "SR"
    SSR = "SSR"


class QualityEnum(StrEnum):
    COMMON = "COMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDRY = "LEGENDRY"
    RED = "RED"


class ElementEnum(StrEnum):
    PHYSICS = "Physics"
    PHYSICS_FLAME = "Physics-Flame"

    FLAME = "Flame"
    FLAME_PHYSICS = "Flame-Physics"

    ICE = "Ice"
    ICE_THUNDER = "Ice-Thunder"

    THUNDER = "Thunder"
    THUNDER_ICE = "Thunder-Ice"

    SUPERPOWER = "SuperPower"


class CategoryEnum(StrEnum):
    DPS = "DPS"
    SUP = "SUP"
    TANK = "Tank"


class EmojisEnum(Enum):
    CommonAtkAdded = PartialEmoji(name="CommonAtkAdded", id=1309607414231990312)
    MaxHealthAdded = PartialEmoji(name="MaxHealthAdded", id=1309607643857551450)
    CritAdded = PartialEmoji(name="CritAdded", id=1309607819221270709)
    ElementDef = PartialEmoji(name="ElementDef", id=1309608549403463721)

    DPS = PartialEmoji(name="DPS", id=1309612783436042272)
    SUP = PartialEmoji(name="SUP", id=1309613003989323777)
    Tank = PartialEmoji(name="Tank", id=1309612877576933436)

    Physics = PartialEmoji(name="Physics", id=1309613593242898572)
    PhysicsFlame = PartialEmoji(name="PhysicsFlame", id=1309613524435337267)

    Flame = PartialEmoji(name="Flame", id=1309613363717865584)
    FlamePhysics = PartialEmoji(name="FlamePhysics", id=1309613413181161593)

    Ice = PartialEmoji(name="Ice", id=1309613309544370176)
    ThunderIce = PartialEmoji(name="ThunderIce", id=1309613162814771293)

    Thunder = PartialEmoji(name="Thunder", id=1309613095945109545)
    IceThunder = PartialEmoji(name="IceThunder", id=1309613238950035517)

    SuperPower = PartialEmoji(name="SuperPower", id=1309658479967076352)

    BallGold = PartialEmoji(name="BallGold", id=1309657766008197150)
    BallBlack = PartialEmoji(name="BallBlack", id=1309657709477367828)
    BallRed = PartialEmoji(name="BallRed", id=1309657895578767411)
    BallsMixed = PartialEmoji(name="BallsMixed", id=1309658158901235712)

    SparklingHeart = "\U0001f496"
    BrokenHeart = "\U0001f494"

    SmallRedTriangleUp = "\U0001f53a"
    SmallRedTriangleDown = "\U0001f53b"

    Star = "\U00002b50"
    GlowingStar = "\U0001f31f"
    DarkStar = "★"

    def __str__(self) -> str:
        return str(self.value)


def _convert_tag_to_markdown(value: str) -> str:
    pattern = r"<shuzhi>(.*?)</>"
    return re.sub(pattern, r"**\1**", value)


ParseRegex = Annotated[str, AfterValidator(_convert_tag_to_markdown)]
