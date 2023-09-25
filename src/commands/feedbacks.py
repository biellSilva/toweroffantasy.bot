import discord

from discord.ext import commands
from discord import app_commands
from time import time
from asyncio import TimeoutError

from src.config import BOT_GUILD, FEEDBACK_CATEGORY

timeout = 500


class Feedback(commands.Cog):

    '''Feedback Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='feedback')
    async def feedbacks(self, interaction: discord.Interaction):
        '''
        Suggestions, bug reports, words of encouragement, feel free to tell me what you need.
        '''
        await interaction.response.defer(ephemeral=True)

        dm_channel = await interaction.user.create_dm()

        em_1 = discord.Embed(color=discord.Colour.dark_embed(),
                             description=f'Check your dm {dm_channel.jump_url}')

        em = discord.Embed(color=discord.Colour.dark_embed(), title = 'Feedback',
                           description = (f'A feedback can be suggestions, bug reports, words of encouragement, whatever you like, feel free to tell me what you need.\n'
                          f'Send a message with all you want, it can contains everything you can send in one message\n\n'
                          f'This interaction has a `waiting cooldown` to be finished: <t:{int(time()+timeout)}:R>'))
        em.set_thumbnail(url=self.bot.user.avatar.url)
        
        await dm_channel.send(embed=em)
        await interaction.edit_original_response(embed=em_1)

        def check(message: discord.Message):
            return message.channel == dm_channel

        try:
            feedback = await self.bot.wait_for('message', timeout=timeout, check=check)
        except TimeoutError:
            return await dm_channel.send('timeout expired, feedback canceled')

        em_res = discord.Embed(color=discord.Colour.dark_embed(), 
                               description=feedback.content)
        
        em_res.set_author(name=f'{feedback.author} - {feedback.author.id}', 
                          icon_url=feedback.author.display_avatar.url, 
                          url=feedback.author.dm_channel.jump_url)
        
        await dm_channel.send(embed=em_res, 
                              content=(f'*This is an example of your feedback and how many files it has, type **`confirm`** and it will be sent*\n'
                                       f'**{len(feedback.attachments)} files**'))
        
        def check(message: discord.Message):
            return message.channel == dm_channel and message.content.lower() == 'confirm'

        try:
            response = await self.bot.wait_for('message', timeout=timeout, check=check)
        except TimeoutError:
            return await dm_channel.send('timeout expired, submission canceled')
        
        guild = self.bot.get_guild(BOT_GUILD)
        category = guild.get_channel(FEEDBACK_CATEGORY)
        feedback_channel = await category.create_text_channel(name=f'feedback n{len(category.channels)+1}')

        files_url = '\n'.join([file.url for file in feedback.attachments])

        await feedback_channel.send(content=files_url if files_url else None, embed=em_res)
        await response.add_reaction('✅')

async def setup(bot: commands.Bot):
    await bot.add_cog(Feedback(bot))
