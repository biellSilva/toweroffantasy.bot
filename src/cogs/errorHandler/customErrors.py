


from discord.ext import commands


class DataNotFound(commands.CommandError):
    def __init__(self, name: str) -> None:
        self.name = name
        self.message = f'**{name}** not found'
        super().__init__(self.message)


class WrongDatetimeFormat(commands.CommandError):
    def __init__(self, date_str: str, format: str, ) -> None:
        self.date_str = date_str
        self.format = format
        self.message = f'**{date_str}** doesn\'t match with **{format}** format'
        super().__init__(self.message)