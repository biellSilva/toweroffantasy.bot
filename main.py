import discord
import dotenv
import os

from discord.ext import commands

from src.service.sync_data import update_cache


class Dumbot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix = 't!', 
                         intents = discord.Intents.all(), 
                         case_insensitive = True, 
                         strip_after_prefix = True,
                         help_command = None)
        
        self.maintenance = False

    async def on_ready(self):
        print(f'{"-"*20}\n'
              f'{self.user}\n'
              f'{self.status} - {round(self.latency * 1000)}ms\n'
              f'{"-"*20}')


    async def setup_hook(self):
        self.task = self.loop.create_task(self.wait_until_ready_tasks())
        await update_cache()

        for folder in os.listdir('./src'):
            if not folder.endswith('.py') and folder.lower() not in ('views'):
                for filename in os.listdir(f'./src/{folder}'):
                    if filename.endswith('.py'):
                        try:
                            await self.load_extension(f'src.{folder}.{filename[:-3]}')
                            print(f'{folder}.{filename[:-3]} loaded')
                        except commands.NoEntryPointError:
                            continue


    async def wait_until_ready_tasks(self):
        await self.wait_until_ready()

        if self.maintenance:
            await self.change_presence(activity=discord.Activity(
                        type=discord.ActivityType.listening,
                        name='MAINTENANCE'),
                        status=discord.Status.dnd
                        )
        else:
            await self.change_presence(activity=discord.Activity(
                        type=discord.ActivityType.listening,
                        name='/help'),
                        status=discord.Status.online
                        )
            
        


bot = Dumbot()

bot.run(token=dotenv.get_key(dotenv_path=dotenv.find_dotenv(), key_to_get='token'))