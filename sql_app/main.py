import pandas
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
from sql_app.models import AutonomousSystem

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/{item_id}", response_model=schemas.AutonomousSystem)
def read_as_by_number(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


df = pandas.read_csv("sql_app/db_data/ip2asn-combined.tsv", sep='\t')
df.to_sql(con=engine, index_label='id', name=AutonomousSystem.__tablename__, if_exists='replace')
