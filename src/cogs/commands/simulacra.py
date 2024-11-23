import discord
from discord import app_commands
from discord.ext import commands

from src.api.simulacra import SimulacraService
from src.auto_complete import AutoCompleteHelper
from src.embeds.simulacra import SimulacrumEmbeds
from src.views.simulacra import SimulacraView


class SimulacrumCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.api = SimulacraService()
        self.auto_complete = AutoCompleteHelper()

    @app_commands.command(name="simulacrum", description="Get simulacrum information")
    @app_commands.rename(simulacrum_id="id")
    @app_commands.describe(simulacrum_id="Simulacrum ID")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.allowed_installs(guilds=True, users=True)
    async def simulacrum_command(
        self, interaction: discord.Interaction, simulacrum_id: str
    ) -> None:
        imitation = await self.api.get_id(interaction.locale, simulacrum_id)

        controller = SimulacrumEmbeds(imitation)

        await interaction.response.send_message(
            embeds=controller.imitation_embed(),
            view=SimulacraView(owner=interaction.user, controller=controller),
        )

    @simulacrum_command.autocomplete("simulacrum_id")
    async def simulacrum_id_autocomplete(
        self, interaction: discord.Interaction, current: str
    ) -> list[app_commands.Choice[str]]:
        return await self.auto_complete.simulacrum_id_autocomplete(interaction, current)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SimulacrumCog(bot=bot))
