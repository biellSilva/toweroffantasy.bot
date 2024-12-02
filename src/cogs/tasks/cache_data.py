from discord.ext import commands, tasks

from src.api.matrices import MatricesService
from src.api.simulacra import SimulacraService


class CacheDataCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.simulacra = SimulacraService()
        self.matrices = MatricesService()

    async def on_load(self) -> None:
        pass

    async def on_unload(self) -> None:
        pass

    @tasks.loop(minutes=30)
    async def cache_data(self) -> None:
        await self.simulacra.clear_cache()
        await self.matrices.clear_cache()


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CacheDataCog(bot=bot))
