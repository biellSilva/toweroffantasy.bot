from typing import TYPE_CHECKING, Any, Callable, Union

import discord
from adapters.discord.embeds import simulacra as embeds

if TYPE_CHECKING:
    from domain.models.simulacra import Simulacra


class SimulacraView(discord.ui.View):
    def __init__(
        self,
        *,
        timeout: float | None = 180,
        data: "Simulacra",
        owner: Union[discord.User, discord.Member],
    ):
        self.data = data
        self.owner = owner
        super().__init__(timeout=timeout)

        self.add_item(SimulacraDropdown(owner=owner, data=data))

        # if simulacra.weapon:
        #     self.add_item(SimulacraWeaponButton(owner=owner, simulacra=simulacra))

        # if simulacra.matrix:
        #     self.add_item(SimulacraMatrixButton(owner=owner, simulacra=simulacra))


class SimulacraDropdown(discord.ui.Select[Any]):
    def __init__(
        self,
        *,
        data: "Simulacra",
        owner: Union[discord.User, discord.Member],
    ) -> None:
        self.owner = owner
        self.data = data

        self._options: dict[str, Callable[..., list[discord.Embed]]] = dict(
            sorted(
                {
                    "profile": embeds.profile_embed,
                    "awakening": embeds.awakening_embed,
                    "voice actors": embeds.voice_actors_embed,
                    "fashion": embeds.fashion_embed,
                    "banners": embeds.banners_embed,
                    "guidebook": embeds.guidebook_embed,
                }.items()
            )
        )

        super().__init__(
            custom_id="simulacra_dropdown",
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
            await interaction.edit_original_response(
                embeds=self._options[self.values[0]](self.data)
            )


class SimulacraWeaponButton(discord.ui.Button[Any]):
    def __init__(
        self, *, owner: Union[discord.User, discord.Member], data: "Simulacra"
    ) -> None:
        super().__init__(style=discord.ButtonStyle.grey, label="Weapon")
        self.owner = owner
        self.data = data

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.owner:
            return

        await interaction.response.send_message(
            content=str(self.data.weapon)[:2000], ephemeral=True
        )


class SimulacraMatrixButton(discord.ui.Button[Any]):
    def __init__(
        self, *, owner: Union[discord.User, discord.Member], data: "Simulacra"
    ) -> None:
        super().__init__(style=discord.ButtonStyle.grey, label="Matrix")
        self.owner = owner
        self.data = data

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.owner:
            return

        await interaction.response.send_message(
            content=str(self.data.matrix)[:2000], ephemeral=True
        )
