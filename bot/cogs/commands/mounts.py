import discord

from discord.ext import commands
from discord import app_commands

from bot.core.controller.get_data import get_mount, get_names
from bot.infra.entitys import Mount


class MountsCog(commands.Cog):

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

        await interaction.edit_original_response(embed=mount.embed)

    @mounts.autocomplete(name='name')
    async def mounts_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(
                name=f'{f"[{mount.type}]" if mount.type else ""} {mount.name}' if mount.chinaOnly == False else f'[CN] {f"[{mount.type}]" if mount.type else ""} {mount.name}',
                value=mount.name) 
            for mount in await get_names('mounts') if current.lower() in mount.name.lower() if isinstance(mount, Mount)][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(MountsCog(bot))
