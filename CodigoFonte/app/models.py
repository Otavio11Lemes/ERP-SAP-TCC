from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Ferramenta(Base):
    __tablename__ = 'ferramentas'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(String)
    quantidade = Column(Integer)
    data_aquisicao = Column(DateTime)
    valor_aquisicao = Column(Float)
    local_armazenamento = Column(String)
    observacoes = Column(String)

class Suprimento(Base):
    __tablename__ = 'suprimentos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(String)
    quantidade_disponivel = Column(Integer)
    valor_unitario = Column(Float)
    data_compra = Column(DateTime)
    fornecedor = Column(String)
    observacoes = Column(String)

class Caminhao(Base):
    __tablename__ = 'caminhoes'
    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String)
    placa = Column(String, unique=True, index=True)
    ano = Column(Integer)
    km_rodados = Column(Integer)
    status_manutencao = Column(String)
    observacoes = Column(String)

class Manutencao(Base):
    __tablename__ = 'manutencoes'
    id = Column(Integer, primary_key=True, index=True)
    caminhao_id = Column(Integer, ForeignKey('caminhoes.id'))
    data_agendamento = Column(DateTime)
    tipo_manutencao = Column(String)
    descricao = Column(String)
    custo_estimado = Column(Float)
    custo_real = Column(Float, nullable=True)
    status = Column(String)
    observacoes = Column(String)
    caminhao = relationship("Caminhao")
