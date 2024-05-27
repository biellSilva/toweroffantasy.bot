from typing import TYPE_CHECKING, Any, Callable, Union

import discord
from adapters.discord.embeds import weapons as embeds

if TYPE_CHECKING:
    from domain.models.weapons import Weapon


class WeaponView(discord.ui.View):
    def __init__(
        self,
        *,
        timeout: float | None = 180,
        data: "Weapon",
        owner: Union[discord.User, discord.Member],
    ):
        self.data = data
        self.owner = owner
        super().__init__(timeout=timeout)

        self.add_item(WeaponDropdown(owner=owner, data=data))


class WeaponDropdown(discord.ui.Select[Any]):
    def __init__(
        self,
        *,
        data: "Weapon",
        owner: Union[discord.User, discord.Member],
    ) -> None:
        self.owner = owner
        self.data = data

        self._options: dict[str, Callable[..., list[discord.Embed]]] = dict(
            sorted(
                {
                    "stats": embeds.stats_embed,
                    "effects": embeds.weapon_effects_embed,
                    "fashion": embeds.fashion_embed,
                    "advancements": embeds.advancements_embed,
                    "banners": embeds.banners_embed,
                    "skills": embeds.normal_attacks_embed,
                }.items()
            )
        )

        super().__init__(
            custom_id="weapon_dropdown",
            placeholder="Select an option",
            options=[
                discord.SelectOption(label=item.title(), value=item.lower())
                for item in self._options.keys()
            ],
        )

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        if self.values[0] in self._options:
            if self.values[0] == "skills":
                return await interaction.edit_original_response(
                    embeds=self._options[self.values[0]](self.data),
                    view=SkillsView(data=self.data, owner=self.owner),
                )

            await interaction.edit_original_response(
                embeds=self._options[self.values[0]](self.data),
                view=WeaponView(data=self.data, owner=self.owner),
            )


class SkillsView(discord.ui.View):
    def __init__(
        self,
        *,
        timeout: float | None = 180,
        data: "Weapon",
        owner: Union[discord.User, discord.Member],
    ):
        self.data = data
        self.owner = owner
        super().__init__(timeout=timeout)

        self.add_item(WeaponDropdown(owner=owner, data=data))

        if data.weaponAttacks.normals:
            self.add_item(NormalAttackButton(owner=owner, data=data))

        if data.weaponAttacks.dodge:
            self.add_item(DodgeAttackButton(owner=owner, data=data))

        if data.weaponAttacks.skill:
            self.add_item(SkillsAttackButton(owner=owner, data=data))

        if data.weaponAttacks.discharge:
            self.add_item(DischargeAttackButton(owner=owner, data=data))


class NormalAttackButton(discord.ui.Button[Any]):
    def __init__(
        self, *, owner: Union[discord.User, discord.Member], data: "Weapon"
    ) -> None:
        super().__init__(style=discord.ButtonStyle.grey, label="Normal")
        self.owner = owner
        self.data = data

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(
            embeds=embeds.normal_attacks_embed(self.data)
        )


class DodgeAttackButton(discord.ui.Button[Any]):
    def __init__(
        self, *, owner: Union[discord.User, discord.Member], data: "Weapon"
    ) -> None:
        super().__init__(style=discord.ButtonStyle.grey, label="Dodge")
        self.owner = owner
        self.data = data

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(
            embeds=embeds.dodge_attacks_embed(self.data)
        )


class SkillsAttackButton(discord.ui.Button[Any]):
    def __init__(
        self, *, owner: Union[discord.User, discord.Member], data: "Weapon"
    ) -> None:
        super().__init__(style=discord.ButtonStyle.grey, label="Skills")
        self.owner = owner
        self.data = data

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(
            embeds=embeds.skills_attacks_embed(self.data)
        )


class DischargeAttackButton(discord.ui.Button[Any]):
    def __init__(
        self, *, owner: Union[discord.User, discord.Member], data: "Weapon"
    ) -> None:
        super().__init__(style=discord.ButtonStyle.grey, label="Discharge")
        self.owner = owner
        self.data = data

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(
            embeds=embeds.discharge_attacks_embed(self.data)
        )
