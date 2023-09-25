import discord

from discord.ext import commands
from discord import app_commands

from src.config import base_url_dict
from src.controller.get_data import get_matrice


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
    async def matrices(self, interaction: discord.Interaction, name: str):
        '''
        Matrices (aka Chips) are items that can be attached to weapon slots.
        '''

        await interaction.response.defer()

        matrice = await get_matrice(name=name)

        china = '[CN]' if matrice.chinaOnly else ''

        em = discord.Embed(color=discord.Colour.dark_embed(), 
                           title=f'{matrice.name} {matrice.rarity} {china}')
        
        em.url = base_url_dict['matrice_home'] + matrice.name.replace(' ', '-').lower()
        em.set_thumbnail(url=matrice.imgSrc)

        for set_ in matrice.sets:
            em.add_field(name=f'{set_.pieces}x Pieces', value=set_.description, inline=False)

        await interaction.edit_original_response(embed=em)
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Matrices(bot))
