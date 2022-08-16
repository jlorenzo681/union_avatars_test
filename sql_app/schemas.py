from pydantic import BaseModel


class AutonomousSystemBase(BaseModel):
    range_start: str
    range_end: str
    AS_number: str
    country_code: str | None = None
    AS_description: str | None = None


class AutonomousSystemCreate(AutonomousSystemBase):
    pass


class AutonomousSystem(AutonomousSystemBase):
    id: int

    class Config:
        orm_mode = True

