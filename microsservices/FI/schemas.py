from pydantic import BaseModel

class FinancialRecordBase(BaseModel):
    description: str
    amount: float

class FinancialRecordCreate(FinancialRecordBase):
    pass

class FinancialRecord(FinancialRecordBase):
    id: int

    class Config:
        orm_mode = True