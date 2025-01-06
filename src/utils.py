from discord import Colour, Locale, PartialEmoji

from src.types import EmojisEnum, LangsEnum


def convert_locale(lang: Locale) -> LangsEnum:
    _locales = {
        Locale.american_english: LangsEnum.EN,
        Locale.british_english: LangsEnum.EN,
        Locale.french: LangsEnum.FR,
        Locale.german: LangsEnum.DE,
        Locale.latin_american_spanish: LangsEnum.ES,
        Locale.spain_spanish: LangsEnum.ES,
        Locale.brazil_portuguese: LangsEnum.PT,
        Locale.japanese: LangsEnum.JA,
        Locale.thai: LangsEnum.TH,
        Locale.chinese: LangsEnum.ZH_CN,
        Locale.indonesian: LangsEnum.ID,
        Locale.russian: LangsEnum.RU,
    }
    return _locales.get(lang, LangsEnum.EN)


def convert_rarity_to_int(rarity: str) -> int:
    _rarities = {
        "N": 1,
        "R": 2,
        "SR": 3,
        "SSR": 4,
    }
    return _rarities.get(rarity, 0)


def convert_rarity_to_str(rarity: int) -> str:
    _rarities = {
        1: "N",
        2: "R",
        3: "SR",
        4: "SSR",
    }
    return _rarities.get(rarity, "Unknown")


def convert_quality_to_color(quality: str) -> Colour:
    _qualities = {
        "COMMON": Colour.dark_grey(),
        "RARE": Colour.dark_blue(),
        "EPIC": Colour.dark_purple(),
        "LEGENDARY": Colour.dark_gold(),
        "LEGENDRY": Colour.dark_gold(),
        "RED": Colour.dark_red(),
    }
    return _qualities.get(quality, Colour.dark_theme())


def convert_rarity_to_color(rarity: str) -> Colour:
    _rarities = {
        "N": Colour.dark_grey(),
        "R": Colour.dark_blue(),
        "SR": Colour.dark_purple(),
        "SSR": Colour.dark_gold(),
    }
    return _rarities.get(rarity, Colour.dark_theme())


def convert_to_emoji(value: str) -> str:
    value = value.replace(" ", "").replace("-", "")
    if value in EmojisEnum.__members__:
        return str(EmojisEnum[value])
    return str(PartialEmoji(name=value, id=None))


def get_limited_emoji(limited: bool) -> str:
    return str(EmojisEnum.BallRed) if limited else str(EmojisEnum.BallsMixed)


def split_matrix_name(name: str) -> str:
    if ":" in name:
        return name.split(":")[0]

    if "・" in name:
        return name.split("・")[0]

    return name
