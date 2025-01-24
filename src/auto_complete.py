from typing import Self

from discord import Interaction
from discord.app_commands import Choice
from unidecode import unidecode

from src.api.matrices import MatricesService
from src.api.simulacra import SimulacraService
from src.api.weapons import WeaponService
from src.types import QualityEnum, RarityEnum
from src.utils import convert_locale, convert_rarity_to_int, split_matrix_name


class AutoCompleteHelper:
    __instance: Self | None = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.matrices = MatricesService()
        self.simulacra = SimulacraService()
        self.weapons = WeaponService()

    async def matrix_id_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:
        data = sorted(
            filter(
                lambda x: "L1" not in x.id,
                await self.matrices.get_all_from_cache(
                    lang=convert_locale(interaction.locale)
                ),
            ),
            key=lambda x: (
                -convert_rarity_to_int(x.matrices[0].rarity),
                unidecode(split_matrix_name(x.matrices[0].name)),
            ),
        )

        for char in current.split():
            if unidecode(char).upper() in RarityEnum:
                data = list(
                    filter(
                        lambda x: unidecode(x.matrices[0].rarity).lower()
                        == unidecode(char).lower(),
                        data,
                    )
                )
                continue

            if unidecode(char).upper() in QualityEnum:
                data = list(
                    filter(
                        lambda x: unidecode(char).lower()
                        in unidecode(x.matrices[0].quality).lower()
                        or unidecode(char).lower() in unidecode(x.quality).lower(),
                        data,
                    )
                )
                continue

            data = list(
                filter(
                    lambda x: unidecode(char).lower()
                    in unidecode(x.matrices[0].name).lower(),
                    data,
                )
            )

        return [
            Choice(
                name=f"[{matrix.matrices[0].rarity}] {split_matrix_name(matrix.matrices[0].name)}",
                value=matrix.id,
            )
            for matrix in data
        ][:25]

    async def simulacrum_id_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:
        data = sorted(
            await self.simulacra.get_all_from_cache(
                lang=convert_locale(interaction.locale)
            ),
            key=lambda x: (
                -convert_rarity_to_int(x.rarity),
                unidecode(x.name),
            ),
        )

        for char in current.split():
            if unidecode(char).upper() in RarityEnum:
                data = list(
                    filter(
                        lambda x: unidecode(x.rarity).lower()
                        == unidecode(char).lower(),
                        data,
                    )
                )
                continue

            data = list(
                filter(
                    lambda x: unidecode(char).lower() in unidecode(x.name).lower()
                    or unidecode(char).lower() in unidecode(x.id).lower()
                    or (
                        x.weapon_id
                        and unidecode(char).lower() in unidecode(x.weapon_id).lower()
                    )
                    or unidecode(char).lower() in unidecode(x.avatar_id).lower()
                    or unidecode(char).lower() in unidecode(x.sex).lower(),
                    data,
                )
            )

        return [
            Choice(
                name=f"[{data.rarity}] {data.name}",
                value=data.id,
            )
            for data in data
            if "L1" not in data.id
        ][:25]

    async def weapon_id_autocomplete(self, interaction: "Interaction", current: str):
        data = sorted(
            filter(
                lambda x: x.is_warehouse,
                await self.weapons.get_all_from_cache(
                    lang=convert_locale(interaction.locale)
                ),
            ),
            key=lambda x: (
                -convert_rarity_to_int(x.rarity),
                unidecode(x.name),
            ),
        )

        for char in current.split():
            if unidecode(char).upper() in RarityEnum:
                data = list(
                    filter(
                        lambda x: unidecode(x.rarity).lower()
                        == unidecode(char).lower(),
                        data,
                    )
                )
                continue

            data = list(
                filter(
                    lambda x: unidecode(char).lower() in unidecode(x.name).lower(),
                    data,
                )
            )

        return [
            Choice(
                name=f"[{weapon.rarity}] {weapon.name}",
                value=weapon.id,
            )
            for weapon in data
        ][:25]
