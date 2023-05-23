import discord

from discord.ext import commands
from discord import app_commands

from src.config import db_client


class Matrices(commands.Cog):

    '''Matrices Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='matrices')
    async def matrices(self, interaction: discord.Interaction, name: str):
        pass

    
async def setup(bot):
    await bot.add_cog(Matrices(bot))
