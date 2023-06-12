import discord

from discord.ext import commands
from discord import app_commands
from time import time

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
        await interaction.response.defer(ephemeral=True)

        if interaction.user != self.bot.application.owner:
            raise NotImplementedError()
        
        em = discord.Embed(color=no_bar)

        dm_channel = await interaction.user.create_dm()

        em.description=f'Check your dm {dm_channel.jump_url}'
        await interaction.edit_original_response(embed=em)

        em.title = 'Feedback'
        em.description = (f'A feedback can be suggestions, bug reports, words of encouragement, whatever you like, feel free to tell me what you need.\n'
                          f'Send a message with all you want, it can contains everything you can send in one message\n\n'
                          f'This interaction has a `waiting cooldown` to be finished: <t:{int(time()+500)}:R>')
        
        em.set_thumbnail(url=self.bot.user.avatar.url)
        
        await dm_channel.send(embed=em)
        
    
async def setup(bot):
    await bot.add_cog(Feedback(bot))
