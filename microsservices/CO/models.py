from sqlalchemy import Column, Integer, String, Float
from database import Base

# Existing FinancialRecord model
class FinancialRecord(Base):
    __tablename__ = "vendor"

    id = Column(Integer, primary_key=True, index=True)
    nature = Column(String, index=True)
    enterprise_name = Column(String, index=True)
    phone = Column(String, index=True)
    email = Column(String, index=True)

    #teste
    