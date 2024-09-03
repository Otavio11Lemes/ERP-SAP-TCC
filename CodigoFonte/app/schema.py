from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FerramentaBase(BaseModel):
    nome: str
    tipo: str
    quantidade: int
    data_aquisicao: datetime
    valor_aquisicao: float
    local_armazenamento: str
    observacoes: Optional[str] = None

class FerramentaCreate(FerramentaBase):
    pass

class Ferramenta(FerramentaBase):
    id: int

    class Config:
        orm_mode = True

# Esquemas para Suprimento, Caminhao, Manutencao seguem a mesma estrutura...
