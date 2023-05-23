import discord
import requests

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, simulacra_collection
from src.utils import check_name
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
        
        url_name = name.replace(' ', '-').lower()
        em.url = f'https://toweroffantasy.info/simulacra/{url_name}'

        for name in [simulacra['name'], simulacra['cnName']]:
            base_url = 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/huanxing/lihui/'
            re_1 = requests.get(f'{base_url}{name}.webp')
            re_2 = requests.get(f'{base_url}{name.lower()}.webp')

            if re_1.status_code == 200:
                em.set_thumbnail(url=str(re_1.url))
            if re_2.status_code == 200:
                em.set_thumbnail(url=str(re_2.url))

        for region, voiceActor in simulacra['voiceActors'].items():
            if voiceActor == '':
                continue
            em.add_field(name=region.upper(), value=voiceActor, inline=True)

        await interaction.edit_original_response(embed=em, view=MainView())

    
async def setup(bot):
    await bot.add_cog(Simulacra(bot))
