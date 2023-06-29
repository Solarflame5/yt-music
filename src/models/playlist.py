from __future__ import annotations

from dataclasses import dataclass

from track import Track


@dataclass
class Playlist:
    id: str
    privacy: str
    title: str
    thumbnails: list
    description: str
    author: str
    duration: str
    duration_seconds: int
    track_count: int
    suggestions: list
    related: list[Playlist]
    tracks: list[Track]
