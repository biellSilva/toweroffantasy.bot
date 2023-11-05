


from discord.ext.commands import HybridCommandError
from discord.app_commands import AppCommandError


class DataNotFound(AppCommandError):
    def __init__(self, name: str) -> None:
        self.name = name
        self.message = f'**{name}** not found'
        super().__init__(self.message)