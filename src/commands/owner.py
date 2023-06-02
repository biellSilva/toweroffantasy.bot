
from discord.ext import commands


class Owner(commands.Cog):

    '''Owner Commands'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='sync')
    @commands.is_owner()
    async def sync(self, ctx: commands.Context):
        async with ctx.typing():
            sync = await ctx.bot.tree.sync()
            await ctx.reply(f'{len(sync)} commands synced')


async def setup(bot):
    await bot.add_cog(Owner(bot))
