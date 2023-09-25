import discord

from discord.ext import commands
from discord import app_commands

from src.views.servant_view import ServantView
from src.models import SmartServant
from src.controller.get_data import get_servant, get_names



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

        em = discord.Embed(color=discord.Colour.dark_embed(), 
                           title=servant.name,
                           description=f'{servant.type_emoji} {servant.element_emoji}\n'
                                       f'Attack: **{servant.attack}** \n'
                                       f'Crit: **{servant.crit}** \n\n'
                                       f'{servant.description}')
        
        em.set_thumbnail(url=servant.imgSrc)

        await interaction.edit_original_response(embed=em, view=ServantView(servant=servant))

    @servant.autocomplete(name='name')
    async def servant_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice]:
        servants_: list[SmartServant] = await get_names('smart-servants')
        return [
            app_commands.Choice(
                name=servant.name,
                value=servant.name)
            for servant in servants_ if current.lower() in servant.name.lower()][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Servants(bot))
