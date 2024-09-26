from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/financial_records/", response_model=schemas.FinancialRecord)
def create_financial_record(financial_record: schemas.FinancialRecordCreate, db: Session = Depends(get_db)):
    return crud.create_financial_record(db=db, financial_record=financial_record)

@app.get("/financial_records/{record_id}", response_model=schemas.FinancialRecord)
def read_financial_record(record_id: int, db: Session = Depends(get_db)):
    db_record = crud.get_financial_record(db, record_id=record_id)
    if db_record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return db_record

@app.get("/financial_records/", response_model=List[schemas.FinancialRecord])
def read_financial_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    records = crud.get_financial_records(db, skip=skip, limit=limit)
    return records