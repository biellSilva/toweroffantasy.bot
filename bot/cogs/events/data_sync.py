
import datetime

from discord.ext import commands, tasks

from bot.core.service.sync_data import update_cache


class EventsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        self.sync_data.start()
        return await super().cog_load()
    
    async def cog_unload(self):
        self.sync_data.stop()
        return await super().cog_unload()
    
    @tasks.loop(
        time=[
            datetime.time(hour=0, minute=0),
            datetime.time(hour=3, minute=0),
            datetime.time(hour=6, minute=0),
            datetime.time(hour=9, minute=0),
            datetime.time(hour=12, minute=0),
            datetime.time(hour=15, minute=0),
            datetime.time(hour=18, minute=0),
            datetime.time(hour=21, minute=0),
            ], 
        reconnect=True)
    async def sync_data(self):
        
        await update_cache()



async def setup(bot: commands.Bot):
     await bot.add_cog(EventsCog(bot))