from adapters.discord.utils import convert_locale
from discord import Interaction, app_commands
from discord.app_commands import Choice
from discord.ext import commands
from infra.repositories.mounts import MountsRepository
from unidecode import unidecode

from adapters.discord.views.mounts import MountsView

from ...embeds.mounts import info_embed


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class MountsCog(
    commands.GroupCog, group_name="mounts", description="Mounts group command"
):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.repository = MountsRepository()

    @app_commands.command(name="global", description="Mounts global command")
    async def mounts_global_command(self, interaction: Interaction, id: str):
        await interaction.response.defer()

        data = await self.repository.get(
            id=id, lang=convert_locale(interaction.locale), version="global"
        )

        await interaction.edit_original_response(
            embeds=info_embed(data),
            view=MountsView(
                data=data,
                owner=interaction.user,
            ),
        )

    @app_commands.command(name="china", description="Mounts china command")
    async def mounts_chinese_command(self, interaction: Interaction, id: str):
        await interaction.response.defer()

        data = await self.repository.get(id=id, lang="cn", version="china")

        await interaction.edit_original_response(
            embeds=info_embed(data),
            view=MountsView(
                data=data,
                owner=interaction.user,
            ),
        )

    @mounts_global_command.autocomplete(name="id")
    async def mounts_global_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:

        return [
            Choice(name=data.name_with_rarity, value=data.id)
            for data in await self.repository.get_all_simple(
                lang=convert_locale(interaction.locale), version="global"
            )
            if unidecode(current).lower() in unidecode(data.name).lower()
            or unidecode(current).lower() in data.id.lower()
            or unidecode(current).lower() == data.rarity_string.lower()
        ][:25]

    @mounts_chinese_command.autocomplete(name="id")
    async def mounts_chinese_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:

        return [
            Choice(name=data.name_with_rarity, value=data.id)
            for data in await self.repository.get_all_simple(lang="cn", version="china")
            if unidecode(current).lower() in unidecode(data.name).lower()
            or unidecode(current).lower() in data.id.lower()
            or unidecode(current).lower() == data.rarity_string.lower()
        ][:25]


async def setup(bot: commands.Bot):
    await bot.add_cog(MountsCog(bot))
