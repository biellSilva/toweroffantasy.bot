from pydantic import BaseModel


class MatrixAsset(BaseModel):
    icon: str | None
    iconLarge: str | None
    characterArtwork: str | None = None


class MatrixSet(BaseModel):
    need: int
    description: str


class MatrixMeta(BaseModel):
    recommendedWeapons: list[str] = []
