from sqlalchemy.orm import Session
import models, schemas

# New CRUD operations for Vendor
def create_vendor(db: Session, vendor: schemas.ReceiverCreate):
    db_vendor = models.Receiver(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

def get_vendor(db: Session, vendor_id: int):
    return db.query(models.vendor).filter(models.vendor.id == vendor_id).first()

def get_vendor(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.vendor).offset(skip).limit(limit).all()