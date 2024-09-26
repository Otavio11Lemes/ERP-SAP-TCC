from sqlalchemy.orm import Session
from . import models, schemas

def create_financial_record(db: Session, financial_record: schemas.FinancialRecordCreate):
    db_financial_record = models.FinancialRecord(**financial_record.dict())
    db.add(db_financial_record)
    db.commit()
    db.refresh(db_financial_record)
    return db_financial_record

def get_financial_record(db: Session, record_id: int):
    return db.query(models.FinancialRecord).filter(models.FinancialRecord.id == record_id).first()

def get_financial_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.FinancialRecord).offset(skip).limit(limit).all()