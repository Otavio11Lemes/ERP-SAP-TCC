from pydantic import BaseModel

# New Receiver models
class VendorBase(BaseModel):
    nature: str
    id_code: int
    enterprise_name: str
    phone: str
    email: str

class VendorCreate(VendorBase):
    pass

class Vendor(VendorBase):
    id: int

    class Config:
        orm_mode = True