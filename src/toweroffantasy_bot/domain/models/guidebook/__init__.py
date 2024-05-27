from domain.models.base import EntityBase

from .extra import GuideBookItem


class GuideBook(EntityBase):
    name: str
    icon: str
    items: list[GuideBookItem]
    menuId: str
    menuType: str
