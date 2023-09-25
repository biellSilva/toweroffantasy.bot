import discord

from discord.ext import commands
from discord import app_commands
from typing import TYPE_CHECKING

from src.controller.get_data import get_simulacra, get_names
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
                           description='')

        if simulacra.cnName and simulacra.cnName not in ('', ' ', '???'):
            em.description += f"**CN Name:** {simulacra.cnName.capitalize()}\n"
            
        if simulacra.gender and simulacra.gender not in ('', ' ', '???'):
            em.description += f"**Gender:** {simulacra.gender}\n"

        if simulacra.height and simulacra.height not in ('', ' ', '???'):
            em.description += f"**Height:** {simulacra.height}\n"

        if simulacra.birthday and simulacra.birthday not in ('', ' ', '???'):
            em.description += f"**Birthday:** {simulacra.birthday}\n"

        if simulacra.birthplace and simulacra.birthplace not in ('', ' ', '???'):
            em.description += f"**Birthplace:** {simulacra.birthplace}\n"

        if simulacra.horoscope and simulacra.horoscope not in ('', ' ', '???'):
            em.description += f"**Horoscope:** {simulacra.horoscope}\n"

        if simulacra.skinsPreviewUrl:
            em.description += f'\n[Skin Preview]({simulacra.skinsPreviewUrl})'
        
        if simulacra.skinsPreviewUrl:
            em.description += f'\n[Skin Preview]({simulacra.skinsPreviewUrl})'
        
        em.url = base_url_dict['simulacra_home'] + simulacra.name.replace(' ', '-').lower()
        em.set_thumbnail(url=await simulacra.simulacra_image())

        for region, voiceActor in simulacra.voiceActors.model_dump().items():
            if voiceActor == '' or voiceActor == None:
                continue
            em.add_field(name=region.upper(), value=voiceActor, inline=True)

        await interaction.edit_original_response(embed=em, view=MainView(simulacra=simulacra))

    @simulacra.autocomplete(name='name')
    async def simulacra_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice]:
        simulacras = await get_names('simulacras')
        return [
            app_commands.Choice(
                name=f'{simu.name} {simu.rarity}' if simu.chinaOnly == False else f'{simu.name} {simu.rarity} [CN]',
                value=simu.name) 
            for simu in simulacras if current.lower() in simu.name.lower()][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Simulacra(bot))
