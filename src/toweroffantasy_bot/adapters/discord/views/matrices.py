from typing import TYPE_CHECKING, Any, Callable, Union

import discord
from adapters.discord.embeds import matrices as embeds

if TYPE_CHECKING:
    from domain.models.matrices import Matrix


class MatricesView(discord.ui.View):
    def __init__(
        self,
        *,
        timeout: float | None = 180,
        data: "Matrix",
        owner: Union[discord.User, discord.Member],
    ):
        self.data = data
        self.owner = owner
        super().__init__(timeout=timeout)

        self.add_item(MatricesDropdown(owner=owner, data=data))


class MatricesDropdown(discord.ui.Select[Any]):
    def __init__(
        self,
        *,
        data: "Matrix",
        owner: Union[discord.User, discord.Member],
    ) -> None:
        self.owner = owner
        self.data = data

        self._options: dict[str, Callable[..., list[discord.Embed]]] = dict(
            sorted(
                {
                    "info": embeds.info_embed,
                    "set effects": embeds.set_effects_embed,
                    "banners": embeds.banners_embed,
                }.items()
            )
        )

        super().__init__(
            custom_id="matrices_dropdown",
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
