from pydantic import BaseModel
from datetime import datetime


class TagIn(BaseModel):
    tag: str


class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str


class TagOut(BaseModel):
    tag: str
    created: datetime
