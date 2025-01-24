import discord
from discord import app_commands
from discord.ext import commands

from src.api.weapons import WeaponService
from src.auto_complete import AutoCompleteHelper
from src.embeds.weapons import WeaponEmbeds
from src.views.weapons import WeaponsView


class WeaponCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.api = WeaponService()
        self.auto_complete = AutoCompleteHelper()

    @app_commands.command(name="weapon", description="Get weapon information")
    @app_commands.rename(weapon_id="id")
    @app_commands.describe(weapon_id="Weapon ID")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.allowed_installs(guilds=True, users=True)
    async def weapon_command(
        self, interaction: discord.Interaction, weapon_id: str
    ) -> None:
        weapon = await self.api.get_id(interaction.locale, weapon_id)

        embed_controller = WeaponEmbeds(weapon=weapon)

        await interaction.response.send_message(
            embeds=embed_controller.main_embed(),
            view=WeaponsView(controller=embed_controller, owner=interaction.user),
        )

    @weapon_command.autocomplete("weapon_id")
    async def weapon_id_autocomplete(
        self, interaction: discord.Interaction, current: str
    ) -> list[app_commands.Choice[str]]:
        return await self.auto_complete.weapon_id_autocomplete(interaction, current)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WeaponCog(bot=bot))
