import discord

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, base_url_dict
from src.utils import check_name, get_data
from src.views.views import MainView


class Simulacra(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='simulacras')
    @app_commands.describe(name='Simulacra name')
    async def simulacra(self, interaction: discord.Interaction, name: str):

        '''
        Simulacra (aka Mimics) are the player's representation of the characters found in Tower of Fantasy.
        '''

        await interaction.response.defer()

        simulacra = await get_data(name=name, data='simulacra', src='json')

        if not simulacra:
            await interaction.edit_original_response(embed=discord.Embed(color=no_bar, description=f'couldn\'t find: {name}'))
            return

        skin_url = f"[Skin Preview]({simulacra['skinsPreviewUrl']})" if 'skinsPreviewUrl' in simulacra else ''

        em = discord.Embed(color=no_bar, 
                           title=f'{simulacra["name"]} {simulacra["rarity"]}' if 'chinaOnly' not in simulacra else f'{simulacra["name"]} {simulacra["rarity"]} [CN]',
                           description= f"CN Name: {simulacra['cnName'].capitalize()}\n"

                                        f"Gender: {simulacra['gender']}\n"
                                        f"Height: {simulacra['height']}\n"
                                        f"Birthday: {simulacra['birthday']}\n"
                                        f"Birthplace: {simulacra['birthplace']}\n"
                                        f"Horoscope: {simulacra['horoscope']}\n\n"

                                        f"{skin_url}" )
        
        em.url = base_url_dict['simulacra_home'] + simulacra['name'].replace(' ', '-').lower()

        thumb_url = await get_data(name=(simulacra['name'], simulacra['cnName']), data='simulacra', src='image')
        if thumb_url:
            em.set_thumbnail(url=thumb_url)

        for region, voiceActor in simulacra['voiceActors'].items():
            if voiceActor == '':
                continue
            em.add_field(name=region.upper(), value=voiceActor, inline=True)

        await interaction.edit_original_response(embed=em, view=MainView())

    
async def setup(bot):
    await bot.add_cog(Simulacra(bot))
