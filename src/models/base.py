from msgspec import Struct


class BaseModel(Struct):
    id: str
