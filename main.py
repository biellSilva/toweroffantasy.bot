import discord
import dotenv
import logging

from discord.ext import commands

from bot import wait_until_ready_tasks, load_cogs_by_dir

_log_status = logging.getLogger('tof_info.status')


class TOF_INFO(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix = 't!', 
                         intents = discord.Intents.all(), 
                         case_insensitive = True, 
                         strip_after_prefix = True,
                         help_command = None)
        

    async def on_ready(self):
        _log_status.info(f'{self.user} - {self.status} - {round(self.latency * 1000)}ms')

    async def setup_hook(self):
        self.loop.create_task(wait_until_ready_tasks(self, maintenance=False))
        await load_cogs_by_dir(self)


if __name__ == '__main__':
    if TOKEN := dotenv.get_key(dotenv_path=dotenv.find_dotenv(), key_to_get='TOKEN'):
        bot = TOF_INFO()
        bot.run(token=TOKEN, root_logger=True)