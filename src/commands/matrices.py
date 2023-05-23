import discord

from discord.ext import commands
from discord import app_commands

from src.config import matrice_collection, no_bar
from src.utils import check_name


class Matrices(commands.Cog):

    '''Matrices Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='matrices')
    @app_commands.describe(name='Matrice name')
    async def matrices(self, interaction: discord.Interaction, name: str):

        '''Matrice command'''

        await interaction.response.defer()

        matrice = matrice_collection.find_one({'name': check_name(name)})

        if not matrice:
            await interaction.edit_original_response(embed=discord.Embed(color=no_bar, 
                                                                         description=f'Couldn\'t find {name}'))
            return
        
        em = discord.Embed(color=no_bar, 
                           title=f'{matrice["name"]} {matrice["rarity"]}' if 'chinaOnly' not in matrice else f'{matrice["name"]} {matrice["rarity"]} [CN]')
        
        for set in matrice['sets']:
            em.add_field(name=f'{set["pieces"]}x', value=set["description"], inline=False)

        await interaction.edit_original_response(embed=em)
    
async def setup(bot):
    await bot.add_cog(Matrices(bot))
