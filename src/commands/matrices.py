import discord

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, base_url_dict
from src.utils import get_git_data, get_image


class Matrices(commands.Cog):

    '''Matrices Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='matrices')
    @app_commands.describe(name='Matrice name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    @app_commands.checks.cooldown(1, 5, key=lambda i: i.user.id)
    async def matrices(self, interaction: discord.Interaction, name: str):
        '''
        Matrices (aka Chips) are items that can be attached to weapon slots.
        '''

        await interaction.response.defer()

        matrice = await get_git_data(name=name, data_folder='matrices', data_type='json')
        thumb_url = await get_image(name=matrice['imgSrc'], data='matrices')

        em = discord.Embed(color=no_bar, 
                           title=f'{matrice["name"]} {matrice["rarity"]}' if 'chinaOnly' not in matrice else f'{matrice["name"]} {matrice["rarity"]} [CN]')
        
        em.url = base_url_dict['matrice_home'] + matrice['name'].replace(' ', '-').lower()

        for set_ in matrice['sets']:
            em.add_field(name=f'{set_["pieces"]}x', value=set_["description"], inline=False)

        if thumb_url:
            em.set_thumbnail(url=thumb_url)

        await interaction.edit_original_response(embed=em)
    
async def setup(bot):
    await bot.add_cog(Matrices(bot))
