import discord

from discord.ext import commands
from typing import Optional

from src.config import no_bar


class Owner(commands.Cog):

    '''Owner Commands'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='sync')
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, spec: Optional[str]):
        async with ctx.typing():
            if spec:
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                sync = []
            else:
                sync = await ctx.bot.tree.sync()
                
            await ctx.reply(f'{len(sync)} commands synced')

    @commands.command(name='check')
    @commands.is_owner()
    async def check_bot(self, ctx: commands.Context):
        async with ctx.typing():
            em = discord.Embed(color=no_bar,
                               title=f'{self.bot.user}',
                               description=f'Status: **{self.bot.status}** \n'
                                           f'Latency: **{round(self.bot.latency * 1000)}ms** \n')
            
            # for future communication if needed
            x = ''
            for guild in self.bot.guilds:
                x += f'{guild.name} - {guild.owner}\n'
                
            em.add_field(name='Guilds', value=x)

            await ctx.send(embed=em)



async def setup(bot):
    await bot.add_cog(Owner(bot))
