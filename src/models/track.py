from dataclasses import dataclass

from album import Album
from artist import Artist


@dataclass
class Track:
    id: str
    title: str
    artists: list[Artist]
    album: list[Album]
