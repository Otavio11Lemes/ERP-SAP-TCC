from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a URL do banco de dados da variável de ambiente DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Verifica se a URL foi carregada corretamente
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL não foi carregada corretamente do arquivo .env")

# Cria o engine do SQLAlchemy usando a URL do banco de dados
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões configurada para não autocommitar e não autoflushar
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base para os modelos ORM
Base = declarative_base()
