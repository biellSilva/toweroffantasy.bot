import discord

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, base_url_dict
from src.utils import check_name, get_data


class Matrices(commands.Cog):

    '''Matrices Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='matrices')
    @app_commands.describe(name='Matrice name')
    async def matrices(self, interaction: discord.Interaction, name: str):

        '''
        Matrices (aka Chips) are items that can be attached to weapon slots.
        '''

        await interaction.response.defer()

        matrice = await get_data(name=name, data='matrices', src='json')

        if not matrice:
            await interaction.edit_original_response(embed=discord.Embed(color=no_bar, 
                                                                         description=f'Couldn\'t find {name}'))
            return
        
        em = discord.Embed(color=no_bar, 
                           title=f'{matrice["name"]} {matrice["rarity"]}' if 'chinaOnly' not in matrice else f'{matrice["name"]} {matrice["rarity"]} [CN]')
        
        em.url = base_url_dict['matrice_home'] + matrice['name'].replace(' ', '-').lower()

        for set in matrice['sets']:
            em.add_field(name=f'{set["pieces"]}x', value=set["description"], inline=False)

        thumb_url = await get_data(name=matrice['imgSrc'], data='matrices', src='image')
        if thumb_url:
            em.set_thumbnail(url=thumb_url)

        await interaction.edit_original_response(embed=em)
    
async def setup(bot):
    await bot.add_cog(Matrices(bot))
