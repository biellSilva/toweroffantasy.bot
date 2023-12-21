
from pydantic import BaseModel
from datetime import datetime


class Banner(BaseModel):
    simulacrumId: str | None
    weaponId: str | None
    matrixId: str | None
    simulacrumName: str | None 
    bannerNumber: int 
    element: str | None 
    category: str | None
    startDate: str
    endDate: str
    detailsLink: str 
    isLimitedBannerOnly: bool 
    isRerun: bool
    isFinalBanner: bool
    isCollab: bool 
    noWeapon: bool


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