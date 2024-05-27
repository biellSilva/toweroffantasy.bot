from datetime import datetime

from pydantic import BaseModel


class MetaLastUpdated(BaseModel):
    username: str
    timestamp: datetime


class RecoMatrix(BaseModel):
    id: str
    pieces: int


class MetaData(BaseModel):
    recommendedPairings: list[str]
    recommendedMatrices: list[RecoMatrix]
    rating: list[float]
    analyticVideoId: str | None
    lastUpdated: MetaLastUpdated
