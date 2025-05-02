from pydantic import BaseModel
from datetime import date
from typing import Optional

class CryptoPriceBase(BaseModel):
    date: date
    price: float
    currency: Optional[str] = 'BTC'

class CryptoPriceCreate(CryptoPriceBase):
    pass

class CryptoPriceRead(CryptoPriceBase):
    id: int

    class Config:
        orm_mode = True