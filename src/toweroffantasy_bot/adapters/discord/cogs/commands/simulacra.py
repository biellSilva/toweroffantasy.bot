from adapters.discord.embeds.simulacra import profile_embed
from adapters.discord.utils import convert_locale
from adapters.discord.views.simulacra import SimulacraView
from discord import Interaction, app_commands
from discord.app_commands import Choice
from discord.ext import commands
from infra.repositories.simulacra import SimulacraRepository
from unidecode import unidecode


class SimulacraCog(
    commands.GroupCog, group_name="simulacra", description="Simulacra group command"
):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.repository = SimulacraRepository()

    @app_commands.command(name="global", description="Simulacra global command")
    async def simulacra_global_command(self, interaction: Interaction, id: str):

        await interaction.response.defer()

        data = await self.repository.get(
            id=id, lang=convert_locale(interaction.locale), version="global"
        )

        await interaction.edit_original_response(
            embeds=profile_embed(data),
            view=SimulacraView(data=data, owner=interaction.user),
        )

    @app_commands.command(name="china", description="Simulacra china command")
    async def simulacra_chinese_command(self, interaction: Interaction, id: str):
        await interaction.response.defer()

        data = await self.repository.get(id=id, lang="cn", version="china")

        await interaction.edit_original_response(
            embeds=profile_embed(data),
            view=SimulacraView(data=data, owner=interaction.user),
        )

    @simulacra_global_command.autocomplete(name="id")
    async def simulacra_global_autocomplete(
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

    @simulacra_chinese_command.autocomplete(name="id")
    async def simulacra_chinese_autocomplete(
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
    await bot.add_cog(SimulacraCog(bot))
