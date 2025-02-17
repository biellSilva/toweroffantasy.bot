from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: str


class BackgroundColor(BaseModel):
    r: float
    g: float
    b: float
    a: float
    hex: str
    hex: str
