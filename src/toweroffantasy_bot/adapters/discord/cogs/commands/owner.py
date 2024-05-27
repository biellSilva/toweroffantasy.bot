from typing import Optional

from discord.ext import commands


class OwnerCog(commands.Cog):
    """Owner Commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="sync")
    @commands.is_owner()
    async def sync(self, ctx: commands.Context[commands.Bot], spec: Optional[str]):
        async with ctx.typing():
            if spec == "clear":
                self.bot.tree.clear_commands(guild=None)
                await self.bot.tree.sync()
                await ctx.reply("commands cleared")

            else:
                sync = await self.bot.tree.sync()
                await ctx.reply(f"{len(sync)} commands synced")


async def setup(bot: commands.Bot):
    await bot.add_cog(OwnerCog(bot))
