import discord

from discord.ext import commands
from discord import app_commands
from typing import TYPE_CHECKING

from src.controller.get_data import get_simulacra
from src.views.simulacra_views import MainView
from src.config import base_url_dict

if TYPE_CHECKING:
    from src.models.simulacra import Simulacra



class Simulacra(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='simulacras')
    @app_commands.describe(name='Simulacra name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def simulacra(self, interaction: discord.Interaction, name: str):

        '''
        Simulacra (aka Mimics) are the player's representation of the characters found in Tower of Fantasy.
        '''

        await interaction.response.defer()

        simulacra = await get_simulacra(name=name)

        china = '[CN]' if simulacra.chinaOnly else ''

        em = discord.Embed(color=discord.Colour.dark_embed(), 
                           title=f'{simulacra.name} {simulacra.rarity} {china}',
                           description= f"**CN Name:** {simulacra.cnName.capitalize()}\n"
                                        f"**Gender:** {simulacra.gender}\n"
                                        f"**Height:** {simulacra.height}\n"
                                        f"**Birthday:** {simulacra.birthday}\n"
                                        f"**Birthplace:** {simulacra.birthplace}\n"
                                        f"**Horoscope:** {simulacra.horoscope}")
        
        if simulacra.skinsPreviewUrl:
            em.description += f'\n\n[Skin Preview]({simulacra.skinsPreviewUrl})'
        
        em.url = base_url_dict['simulacra_home'] + simulacra.name.replace(' ', '-').lower()
        em.set_thumbnail(url=await simulacra.simulacra_image())

        for region, voiceActor in simulacra.voiceActors.model_dump().items():
            if voiceActor == '' or voiceActor == None:
                continue
            em.add_field(name=region.upper(), value=voiceActor, inline=True)

        await interaction.edit_original_response(embed=em, view=MainView(simulacra=simulacra))

    
async def setup(bot: commands.Bot):
    await bot.add_cog(Simulacra(bot))
