from sqlalchemy import Column, Integer, String

from .database import Base


class AutonomousSystem(Base):
    __tablename__ = "autonomous_systems"

    id = Column(Integer, primary_key=True, index=True)
    range_start = Column(String, index=True)
    range_end = Column(String, index=True)
    AS_number = Column(Integer, index=True)
    country_code = Column(String, index=True)
    AS_description = Column(String, index=True)
