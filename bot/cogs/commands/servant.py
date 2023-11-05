import discord

from discord.ext import commands
from discord import app_commands

from bot.core.views.servant_view import ServantView
from bot.infra.entitys import SmartServant
from bot.core.controller.get_data import get_servant, get_names



class Servants(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='servants')
    @app_commands.describe(name='Servant name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def servant(self, interaction: discord.Interaction, name: str):

        '''
        Smart Servants are small robots that aid the player in combat.
        '''

        await interaction.response.defer()

        servant = await get_servant(name=name)

        await interaction.edit_original_response(embed=servant.embed_advanc, view=ServantView(servant=servant, owner=interaction.user))

    @servant.autocomplete(name='name')
    async def servant_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=servant.name, value=servant.name)
            for servant in await get_names('smart-servants') 
            if current.lower() in servant.name.lower() and isinstance(servant, SmartServant)
            ][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Servants(bot))
