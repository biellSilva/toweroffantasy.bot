from typing import Self

from discord import Interaction
from discord.app_commands import Choice
from unidecode import unidecode

from src.api.matrices import MatricesService
from src.api.simulacra import SimulacraService
from src.api.weapons import WeaponService
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
            await self.matrices.get_all_from_cache(
                lang=convert_locale(interaction.locale)
            ),
            key=lambda x: (
                -convert_rarity_to_int(x.rarity),
                unidecode(split_matrix_name(x.matrice_name)),
            ),
        )

        for char in current.split():
            data = list(
                filter(
                    lambda x: unidecode(char).lower()
                    in unidecode(x.matrice_name).lower()
                    or unidecode(char).lower() in unidecode(x.id).lower()
                    or unidecode(char).lower() in unidecode(x.name).lower()
                    or unidecode(char).lower() in unidecode(x.rarity).lower()
                    or unidecode(char).lower() in unidecode(x.matrice_name).lower()
                    or unidecode(char).lower() in unidecode(x.quality).lower(),
                    data,
                )
            )

        return [
            Choice(
                name=f"[{matrix.rarity}] {matrix.name} - {matrix.matrice_name}",
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
            data = list(
                filter(
                    lambda x: unidecode(char).lower() in unidecode(x.id).lower()
                    or unidecode(char).lower() in unidecode(x.name).lower()
                    or unidecode(x.rarity).lower() == unidecode(char).lower()
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
        ][:25]

    async def weapon_id_autocomplete(
        self, interaction: "Interaction", current: str
    ) -> list[Choice[str]]:
        data = sorted(
            await self.weapons.get_all_from_cache(
                lang=convert_locale(interaction.locale)
            ),
            key=lambda x: (
                -convert_rarity_to_int(x.rarity),
                unidecode(x.name),
            ),
        )

        for char in current.split():
            data = list(
                filter(
                    lambda x: unidecode(char).lower() in unidecode(x.id).lower()
                    or unidecode(char).lower() in unidecode(x.name).lower()
                    or unidecode(x.rarity).lower() == unidecode(char).lower()
                    or unidecode(char).lower()
                    in unidecode(x.category.id).replace("-", "").lower()
                    or unidecode(char).lower() in unidecode(x.category.name).lower()
                    or unidecode(char).lower()
                    in unidecode(x.element.id).replace("-", "").lower()
                    or unidecode(char).lower() in unidecode(x.element.name).lower(),
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
