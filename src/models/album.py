from artist import Artist
from base import BaseModel


class Album(BaseModel):
    id: str
    name: str
    artists: list[Artist]
