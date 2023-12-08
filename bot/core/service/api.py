
import aiohttp

from typing import Literal, TypeVar, Generic, Type
from pydantic import BaseModel
from discord import Locale

from bot.cogs.errorHandler.customErrors import DataNotFound
from bot.utils import convert_lang


S = TypeVar('S', bound=BaseModel)
M = TypeVar('M', bound=BaseModel)


class API(Generic[S, M]):
    BASE_URI = 'https://api.toweroffantasy.info'
    def __init__(self, 
                 simple_model: Type[S],
                 model: Type[M],
                 route: Literal[
                     'simulacra', 'weapons',
                     'matrice', 'simulacra-v2',
                     'achievement', 'relic', 
                     'food', 'item', 'outfit'
                    ]) -> None:
        self.route = route
        self.simple_model = simple_model
        self.model = model
    

    async def get(self, id: str, locale: Locale, route: str) -> M:
        lang = convert_lang(locale)
        async with aiohttp.ClientSession(self.BASE_URI) as session:
            async with session.get(f'/{route}/{id}?lang={lang}') as res:
                if res.status == 200:
                    data = await res.json(encoding='utf-8')
                    return self.model(**data)
                
                elif res.status in (404, 422):
                    raise DataNotFound(id)
                
                else:
                    res.raise_for_status()
                    raise Exception(res)
    

    async def get_all(self, locale: Locale, route: str) -> list[S]:
        lang = convert_lang(locale)

        async with aiohttp.ClientSession(self.BASE_URI) as session:
            async with session.get(f'/{route}?lang={lang}') as res:

                if res.status == 200:
                    return [self.simple_model(**i) for i in await res.json()]
                
                else:
                    res.raise_for_status()
                    raise Exception(res)
                
