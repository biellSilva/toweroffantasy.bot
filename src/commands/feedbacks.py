import discord

from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice

from src.config import no_bar


class Feedback(commands.Cog):

    '''Feedback Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='feedback')
    @app_commands.checks.cooldown(1, 10, key=lambda i: i.user.id)
    async def feedbacks(self, interaction: discord.Interaction):
        '''
        Feedback can be suggestions, bug reports, words of encouragement, whatever you like, feel free to tell me what you need.
        '''
        await interaction.response.defer()

        if interaction.user != self.bot.application.owner:
            raise NotImplementedError()

        
        
    
async def setup(bot):
    await bot.add_cog(Feedback(bot))
