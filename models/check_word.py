from pydantic import BaseModel, Field


class CheckWordRequest(BaseModel):
    word1: str = Field(..., min_length=1, description="First word or phrase")
    word2: str = Field(..., min_length=1, description="Second word or phrase")


class CheckWordResponse(BaseModel):
    word1: str
    word2: str
    similarity_score: float
    similarity_percent: float