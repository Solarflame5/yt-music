from dataclasses import dataclass

from artist import Artist


@dataclass
class Album:
    id: str
    name: str
    artists: list[Artist]
