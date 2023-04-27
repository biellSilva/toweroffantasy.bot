import discord
import dotenv

from discord.ext import commands

class Dumbot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix='!', intents=discord.Intents.all())
    
    
