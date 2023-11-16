
from pydantic import BaseModel
from datetime import datetime


class VoiceActors(BaseModel):
    chinese: str | None
    japanese: str | None
    english: str | None
    korean: str | None
    portuguese: str | None


class Awakening(BaseModel):
    name: str
    description: str


class Assets(BaseModel):
    avatar: str | None
    artwork: str | None
    lotteryCard: str | None
    lotteryDrawing: str | None


class Banner(BaseModel):
    bannerNo: int
    start: str
    end: str
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool

    @property
    def __datetime_format(self):
        return '%Y/%m/%d %H:%M'

    @property
    def start_datetime(self):
        try:
            return datetime.strptime(self.start, self.__datetime_format)
        except ValueError:
            return datetime.strptime(self.start, '%Y/%m/%d')
        except:
            raise

    @property
    def end_datetime(self):
        try:
            return datetime.strptime(self.end, self.__datetime_format)
        except ValueError:
            return datetime.strptime(self.end, '%Y/%m/%d')
        except:
            raise