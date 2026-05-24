from typing import Literal

from pydantic import BaseModel, Field


ElementName = Literal["earth", "water", "wind", "fire", "light", "dark"]


class ElementRequest(BaseModel):
    word: str = Field(..., min_length=1, description="Word to classify")


class ElementResponse(BaseModel):
    element: ElementName