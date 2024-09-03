from sqlalchemy.orm import Session
from . import models, schemas

def create_ferramenta(db: Session, ferramenta: schemas.FerramentaCreate):
    db_ferramenta = models.Ferramenta(**ferramenta.dict())
    db.add(db_ferramenta)
    db.commit()
    db.refresh(db_ferramenta)
    return db_ferramenta

def get_ferramenta(db: Session, ferramenta_id: int):
    return db.query(models.Ferramenta).filter(models.Ferramenta.id == ferramenta_id).first()

def get_ferramentas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Ferramenta).offset(skip).limit(limit).all()

# Funções similares para Suprimentos, Caminhoes, e Manutencoes...
