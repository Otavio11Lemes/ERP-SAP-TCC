from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schema, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products/", response_model=schema.Product)
def create_product(product: schema.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@router.get("/products/", response_model=list[schema.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)
