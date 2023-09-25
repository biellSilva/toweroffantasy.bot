import discord
import re

from discord.ext import commands
from discord import app_commands

from src.controller.get_data import get_mount, get_names
from src.models import Mount


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

        mount = await get_mount(name=name)

        em = discord.Embed(color=discord.Colour.dark_embed(), 
                           title=f'{mount.name}' if not mount.chinaOnly else f'{mount.name} [CN]',
                           description='')
        
        em.url = f'https://toweroffantasy.info/mounts/{mount.name.replace(" ", "-").lower()}'
        em.set_thumbnail(url=mount.imgSrc)

        if mount.type:
            em.description += f'**Type:** {mount.type}\n\n'

        for i, part in enumerate(mount.parts):
            result = re.sub(r"\(/([A-Za-z]+(/[A-Za-z]+)+)\.[A-Za-z0-9]+\)", '', part.source, 0, re.MULTILINE)
            result = result.replace('[', '').replace(']', '').replace('<abbr title=\'China Exclusive\'></abbr>', '**[CN]**').replace('\n\n', '\n')

            em.description += f'**Part {i+1}** \n{result}\n'

            if part.dropRate: 
                em.description += f'**Drop rate:** {part.dropRate}\n'

            if part.guide:
                em.description += f'[Guide]({part.guide})\n'

            if part.video:
                em.description += f'[Video Part]({part.video})\n'

            em.description += '\n'

        if mount.videoScr:
            em.description += f'\n[Video Preview]({mount.videoScr})'

        await interaction.edit_original_response(embed=em)

    @mounts.autocomplete(name='name')
    async def mounts_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice]:
        mounts_: list[Mount] = await get_names('mounts')
        return [
            app_commands.Choice(
                name=f'{mount.name} {mount.type}' if mount.chinaOnly == False else f'{mount.name} {mount.type} [CN]',
                value=mount.name) 
            for mount in mounts_ if current.lower() in mount.name.lower()][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Mounts(bot))
