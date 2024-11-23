from discord import Interaction, app_commands
from discord.app_commands import Choice
from discord.ext import commands

from src.api.matrices import MatricesService
from src.auto_complete import AutoCompleteHelper
from src.embeds.matrices import MatrixEmbeds


class MatricesCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.api = MatricesService()
        self.auto_complete = AutoCompleteHelper()

    @app_commands.command(name="matrix", description="Get matrix information")
    @app_commands.rename(matrix_id="id")
    @app_commands.describe(matrix_id="Matrix ID")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.allowed_installs(guilds=True, users=True)
    async def matrix_command(self, interaction: Interaction, matrix_id: str) -> None:
        matrix = await self.api.get_matrix(interaction.locale, matrix_id)

        controller = MatrixEmbeds(matrix)

        await interaction.response.send_message(
            embeds=[controller.sets_embed(), controller.pieces_embed()]
        )

    @matrix_command.autocomplete("matrix_id")
    async def matrix_id_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:
        return await self.auto_complete.matrix_id_autocomplete(interaction, current)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MatricesCog(bot=bot))
