from pydantic import BaseModel


class GuideBookItem(BaseModel):
    title: str
    description: str
    icon: str
