from typing import TYPE_CHECKING, Any, Callable, Union

import discord
from adapters.discord.embeds import mounts as embeds

if TYPE_CHECKING:
    from domain.models.mounts import Mount


class MountsView(discord.ui.View):
    def __init__(
        self,
        *,
        timeout: float | None = 180,
        data: "Mount",
        owner: Union[discord.User, discord.Member],
    ):
        self.data = data
        self.owner = owner
        super().__init__(timeout=timeout)

        self.add_item(MountsDropdown(owner=owner, data=data))


class MountsDropdown(discord.ui.Select[Any]):
    def __init__(
        self,
        *,
        data: "Mount",
        owner: Union[discord.User, discord.Member],
    ) -> None:
        self.owner = owner
        self.data = data

        self._options: dict[str, Callable[..., list[discord.Embed]]] = dict(
            sorted(
                {
                    "info": embeds.info_embed,
                    "parts": embeds.unlock_items_embed,
                }.items()
            )
        )

        super().__init__(
            custom_id="mounts_dropdown",
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
