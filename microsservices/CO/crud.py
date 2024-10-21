from sqlalchemy.orm import Session
import models, schemas

# Existing CRUD operations for FinancialRecord
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

# New CRUD operations for Account
def create_account(db: Session, account: schemas.AccountCreate):
    db_account = models.Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()

def get_accounts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Account).offset(skip).limit(limit).all()

# New CRUD operations for Transaction
def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transaction(db: Session, transaction_id: int):
    return db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

def get_transactions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Transaction).offset(skip).limit(limit).all()

# New CRUD operations for Receiver
def create_receiver(db: Session, receiver: schemas.ReceiverCreate):
    db_receiver = models.Receiver(**receiver.dict())
    db.add(db_receiver)
    db.commit()
    db.refresh(db_receiver)
    return db_receiver

def get_receiver(db: Session, receiver_id: int):
    return db.query(models.Receiver).filter(models.Receiver.id == receiver_id).first()

def get_receivers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Receiver).offset(skip).limit(limit).all()