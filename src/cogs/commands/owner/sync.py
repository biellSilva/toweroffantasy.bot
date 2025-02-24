from typing import Literal

from discord.ext import commands


class OwnerCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="sync", hidden=True)
    @commands.is_owner()
    @commands.max_concurrency(number=1, per=commands.BucketType.default, wait=False)
    async def sync(
        self,
        ctx: commands.Context[commands.Bot],
        spec: Literal["guild", "copy", "clear"] | None = None,
    ) -> None:
        async with ctx.typing():
            if spec == "guild":
                # sync all guild commands for the current context’s guild
                synced = await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Synced {len(synced)} commands to the current guild.")

            elif spec == "copy":
                # copies all global commands to the current guild
                if ctx.guild:
                    self.bot.tree.copy_global_to(guild=ctx.guild)
                    synced = await self.bot.tree.sync(guild=ctx.guild)
                    await ctx.reply(
                        f"Copied {len(synced)} commands to the current guild."
                    )

            elif spec == "clear":
                # remove all global commands from the CommandTree and syncs
                self.bot.tree.clear_commands(guild=None)
                await self.bot.tree.sync()
                await ctx.reply("Cleared all global commands.")

            else:
                # global sync (does not sync guild commands)
                synced = await self.bot.tree.sync()
                await ctx.reply(f"Synced {len(synced)} global commands.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OwnerCog(bot=bot))
