from album import Album
from artist import Artist
from base import BaseModel

from enums.like_status import LikeStatus


class Track(BaseModel):
    id: str
    title: str
    artists: list[Artist]
    album: list[Album]
    duration: str
    like_status: LikeStatus
    thumbnails: list
    is_available: bool
    is_explicit: bool
    video_type: str
    feedback_tokens: dict
