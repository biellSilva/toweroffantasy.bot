
from motor.motor_asyncio import AsyncIOMotorClient as motor
from pymongo.server_api import ServerApi
from dotenv import find_dotenv, get_key

from src.infra.entitys import Guild


MONGO_URI = get_key(find_dotenv(), 'MONGO_URI')
if not MONGO_URI:
    raise Exception('MONGO URI IS MISSING')


class GuildRepository:
    def __init__(self) -> None:
        self.__client = motor(MONGO_URI, server_api=ServerApi('1'))
        self._database = self.__client.tof_info
        self.guilds = self._database.guilds
    
    async def get(self, guild_id: str | int):
        if guild := await self.guilds.find_one(filter={'guild_id': str(guild_id)}):
            return Guild(**guild)
        
        else:
            guild = Guild(guild_id=str(guild_id))
            await self.guilds.insert_one(guild.model_dump())
            return guild
    
    async def get_all(self):
        async for guild in self.guilds.find():
            yield Guild(**guild)
    
    async def update(self, guild: Guild):
        await self.guilds.update_one(filter=guild.mongo_key, update={'$set': guild.model_dump()})
    
    async def delete(self, guild_id: str | int):
        await self.guilds.delete_one(filter={'guild_id': str(guild_id)})

    async def insert(self, guild_id: str | int):
        await self.guilds.insert_one(Guild(guild_id=str(guild_id)).model_dump())