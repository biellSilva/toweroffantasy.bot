import discord
import re

from discord.ext import commands
from discord import app_commands

from src.utils import get_git_data, get_image


class Mounts(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='mounts')
    @app_commands.describe(name='Mount name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def mounts(self, interaction: discord.Interaction, name: str):

        '''
        Mounts are vehicles that help you traverse terrain more quickly.
        '''

        await interaction.response.defer()

        mount: dict = await get_git_data(name=name, data_folder='mounts', data_type='json')
        thumb_url = await get_image(name=mount['imgSrc'], data='mounts')

        em = discord.Embed(color=discord.Colour.dark_embed(), 
                           title=f'{mount["name"]}' if 'chinaOnly' not in mount else f'{mount["name"]} [CN]',
                           description='' if 'type' not in mount else f'Type: **{mount["type"]}**\n\n')

        url_name = mount["name"].replace(' ', '-').lower()
        em.url = f'https://toweroffantasy.info/mounts/{url_name}'
        
        for i, part in enumerate(mount['parts']):
            source:str = part['source']
            regex = r"\(/([A-Za-z]+(/[A-Za-z]+)+)\.[A-Za-z0-9]+\)"
            result = re.sub(regex, '', source, 0, re.MULTILINE)
            result = result.replace('[', '').replace(']', '').replace('<abbr title=\'China Exclusive\'></abbr>', '**[CN]**').replace('\n\n', '\n')

            em.description += f'**Part {i+1}** \n{result}\n'

            if "dropRate" in part: 
                em.description += f"Drop rate {part['dropRate']}\n"

            if 'guide' in part:
                em.description += f'[Guide]({part["guide"]})\n'

            if 'video' in part:
                em.description += f'[Video Part]({part["video"]})\n'

            em.description += '\n'

            
        if 'videoSrc' in part:
            em.description += f'\n[Video Preview]({part["videoSrc"]})'

        if thumb_url:
            em.set_thumbnail(url=thumb_url)

        await interaction.edit_original_response(embed=em)

    
async def setup(bot: commands.Bot):
    await bot.add_cog(Mounts(bot))
