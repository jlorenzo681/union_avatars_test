from pydantic import BaseModel


class ItemBase(BaseModel):
    range_start: str
    range_end: str
    AS_number: str
    country_code: str | None = None
    AS_description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

