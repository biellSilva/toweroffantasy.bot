from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: str


class BackgroundColor(BaseModel):
    r: float
    g: float
    b: float
    a: float
    hex: str


class Pagination[T: BaseModel](BaseModel):
    data: list[T]
    total_items: int
    page: int
    max_page: int
    limit: int
