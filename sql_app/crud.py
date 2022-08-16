from sqlalchemy.orm import Session

from . import models


def get_as(db: Session, as_id: int):
    return db.query(models.AutonomousSystem).filter(models.AutonomousSystem.id == as_id).first()
