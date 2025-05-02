from sqlalchemy import Column, Integer, String, Float, Date, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    price = Column(Float)
    currency = Column(String, index=True)
    __table_args__ = (UniqueConstraint('date', 'currency', name='_date_currency_uc'),)