
from pydantic import BaseModel, Field
from datetime import datetime


class Banner(BaseModel):
    bannerNumber: int
    startDate: str
    endDate: str
    detailsLink: str
    isLimitedBannerOnly: bool
    isRerun: bool
    isFinalBanner: bool
    isCollab: bool
    isPolymorph: bool = Field(alias='noWeapon')

    @property
    def __datetime_format(self):
        return '%Y/%m/%d %H:%M'

    @property
    def start_datetime(self):
        try:
            return datetime.strptime(self.startDate, self.__datetime_format)
        except ValueError:
            return datetime.strptime(self.startDate, '%Y/%m/%d')
        except:
            raise

    @property
    def end_datetime(self):
        try:
            return datetime.strptime(self.endDate, self.__datetime_format)
        except ValueError:
            return datetime.strptime(self.endDate, '%Y/%m/%d')
        except:
            raise