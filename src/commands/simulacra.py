import discord
import requests

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, simulacra_collection, base_url_dict
from src.utils import check_name, check_url
from src.views.views import MainView


class Simulacra(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='simulacra')
    @app_commands.describe(name='Simulacra name')
    async def simulacra(self, interaction: discord.Interaction, name: str):

        '''Simulacra command'''

        await interaction.response.defer()

        simulacra = simulacra_collection.find_one(filter={'name': check_name(name)})

        if simulacra == None:
            await interaction.edit_original_response(embed=discord.Embed(color=no_bar, description=f'couldn\'t find: {name}'))
            return

        skin_url = f"[Skins Preview]({simulacra['skinsPreviewUrl']})" if 'skinsPreviewUrl' in simulacra else ''

        em = discord.Embed(color=no_bar, 
                           title=f'{simulacra["name"]} {simulacra["rarity"]}' if 'chinaOnly' not in simulacra else f'{simulacra["name"]} {simulacra["rarity"]} [CN]',
                           description=f"""
                           CN Name: {simulacra['cnName'].capitalize()}

                           Gender: {simulacra['gender']}
                           Height: {simulacra['height']}
                           Birthday: {simulacra['birthday']}
                           Birthplace: {simulacra['birthplace']}
                           Horoscope: {simulacra['horoscope']}

                           {skin_url} 
                           """)
        
        em.url = base_url_dict['simulacra_url'] + simulacra['name'].replace(' ', '-').lower()

        thumb_url = await check_url('simulacra', names=(simulacra['name'], simulacra['cnName']))
        if thumb_url:
            em.set_thumbnail(url=thumb_url)

        for region, voiceActor in simulacra['voiceActors'].items():
            if voiceActor == '':
                continue
            em.add_field(name=region.upper(), value=voiceActor, inline=True)

        await interaction.edit_original_response(embed=em, view=MainView())

    
async def setup(bot):
    await bot.add_cog(Simulacra(bot))
