import discord

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, base_url_dict
from src.utils import get_git_data, get_image
from src.views.simulacra_views import MainView


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

        simulacra: dict = await get_git_data(name=name, data_folder='simulacra', data_type='json')
        thumb_url = await get_image(name=(simulacra['name'], simulacra['cnName']), data='simulacra')

        skin_url = f"[Skin Preview]({simulacra['skinsPreviewUrl']})" if 'skinsPreviewUrl' in simulacra else ''
        china = '' if 'chinaOnly' not in simulacra else '[CN]'

        em = discord.Embed(color=no_bar, 
                           title=f'{simulacra["name"]} {simulacra["rarity"]} {china}',
                           description= f"CN Name: {simulacra['cnName'].capitalize()}\n"
                                        f"Gender: {simulacra['gender']}\n"
                                        f"Height: {simulacra['height']}\n"
                                        f"Birthday: {simulacra['birthday']}\n"
                                        f"Birthplace: {simulacra['birthplace']}\n"
                                        f"Horoscope: {simulacra['horoscope']}")
        
        if skin_url:
            em.description += f'\n\n{skin_url}'
        
        em.url = base_url_dict['simulacra_home'] + simulacra['name'].replace(' ', '-').lower()

        if thumb_url:
            em.set_thumbnail(url=thumb_url)

        for region, voiceActor in simulacra['voiceActors'].items():
            if voiceActor == '':
                continue
            em.add_field(name=region.upper(), value=voiceActor, inline=True)

        await interaction.edit_original_response(embed=em, view=MainView())

    
async def setup(bot):
    await bot.add_cog(Simulacra(bot))
