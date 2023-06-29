from __future__ import annotations

from base import BaseModel
from track import Track


class Playlist(BaseModel):
    id: str
    privacy: str
    title: str
    thumbnails: list
    description: str
    author: str
    duration: str
    duration_seconds: int
    track_count: int
    suggestions: list[Track]
    related: list[Playlist]
    tracks: list[Track]
