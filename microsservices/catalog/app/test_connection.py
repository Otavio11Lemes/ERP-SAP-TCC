from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a URL do banco de dados da variável de ambiente DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o engine do SQLAlchemy usando a URL do banco de dados
engine = create_engine(DATABASE_URL)

# Testa a conexão com o banco de dados
try:
    with engine.connect() as connection:
        print("Conexão com o banco de dados bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")