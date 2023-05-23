import discord

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, simulacra_collection
from src.views.views import MainView


class Simulacra(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='simulacra')
    @app_commands.describe(name='Simulacra name')
    async def simulacra(self, interaction: discord.Interaction, name: str):

        '''Simulacra command'''

        await interaction.response.defer()

        names = ['Alyss', 'Annabella', 'Bai Ling', 'Baiyuekui', 'Claudia', 'Cobalt-B', 'Cocoritter', 'Crow', 'Echo', 
                 'Ene', 'Fenrir', 'Fiona', 'Frigg', 'Garnett', 'Gnonno', 'Hilda', 'Huma', 'Icarus', 'KING', 'Lan', 'Lin', 
                 'Lyra', 'Marc', 'Meryl', 'Nemesis', 'Pepper', 'Rubilia', 'Ruby', 'Saki Fuwa', 'Samir', 'Shiro', 
                 'Tian Lang', 'Tsubasa', 'Umi', 'Yulan', 'Zero']
        
        for _ in names:
            if name.lower() in _.lower():
                name = _

        simulacra = simulacra_collection.find_one(filter={'name': name})

        if simulacra == None:
            await interaction.edit_original_response(embed=discord.Embed(color=no_bar, description=f'couldn\'t find: {name}'))
            return

        skin_url = f"[Skins Preview]({simulacra['skinsPreviewUrl']})" if 'skinsPreviewUrl' in simulacra else ''

        em = discord.Embed(color=no_bar, title=simulacra['name'] if 'chinaOnly' not in simulacra else f'{simulacra["name"]} [CN]',
                           description=f"""
                           Weapon: {simulacra['weapon']['name']}
                           Rarity: {simulacra['rarity']}
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

        for region, voiceActor in simulacra['voiceActors'].items():
            em.add_field(name=region.upper(), value=voiceActor, inline=True)

        await interaction.edit_original_response(embed=em, view=MainView())

    
async def setup(bot):
    await bot.add_cog(Simulacra(bot))
