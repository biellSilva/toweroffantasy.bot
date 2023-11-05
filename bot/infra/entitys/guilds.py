
from pydantic import BaseModel


class Guild(BaseModel):
    guild_id: str
    group_channel: list[int] | None = None
    roles: list[int] | None = None

    @property
    def mongo_key(self):
        return {'guild_id': self.guild_id}