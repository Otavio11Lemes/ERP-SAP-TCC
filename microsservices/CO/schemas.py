from pydantic import BaseModel

# Existing FinancialRecord models
class FinancialRecordBase(BaseModel):
    description: str
    amount: float

class FinancialRecordCreate(FinancialRecordBase):
    pass

class FinancialRecord(FinancialRecordBase):
    id: int

    class Config:
        orm_mode = True

# New Account models
class AccountBase(BaseModel):
    category: str
    status: str
    type: str

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True

# New Transaction models
class TransactionBase(BaseModel):
    date: str
    value: float
    id_transaction: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True

# New Receiver models
class ReceiverBase(BaseModel):
    nature: str
    id_code: int
    enterprise_name: str
    phone: str
    email: str

class ReceiverCreate(ReceiverBase):
    pass

class Receiver(ReceiverBase):
    id: int

    class Config:
        orm_mode = True