from sqlalchemy import Column, Integer, String, Float
from database import Base

# Existing FinancialRecord model
class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float)

# New Account model
class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    status = Column(String, index=True)
    type = Column(String, index=True)

# New Transaction model
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    value = Column(Float)
    id_transaction = Column(Integer, index=True)

# New Receiver model
class Receiver(Base):
    __tablename__ = "receivers"

    id = Column(Integer, primary_key=True, index=True)
    nature = Column(String, index=True)
    id_code = Column(Integer, index=True)
    enterprise_name = Column(String, index=True)
    phone = Column(String, index=True)
    email = Column(String, index=True)