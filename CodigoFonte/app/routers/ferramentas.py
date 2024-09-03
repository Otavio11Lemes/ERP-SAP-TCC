from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Ferramenta)
def create_ferramenta(ferramenta: schemas.FerramentaCreate, db: Session = Depends(get_db)):
    return crud.create_ferramenta(db=db, ferramenta=ferramenta)

@router.get("/{ferramenta_id}", response_model=schemas.Ferramenta)
def read_ferramenta(ferramenta_id: int, db: Session = Depends(get_db)):
    db_ferramenta = crud.get_ferramenta(db, ferramenta_id=ferramenta_id)
    if db_ferramenta is None:
        raise HTTPException(status_code=404, detail="Ferramenta not found")
    return db_ferramenta

# Rotas para listar, atualizar, e deletar ferramentas, além de rotas para suprimentos e manutenções.
