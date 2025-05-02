from sqlalchemy.orm import Session
from app.models.crypto_price import CryptoPrice
from app.schemas.crypto_price import CryptoPriceCreate
from datetime import date

def get_prices(db: Session):
    return db.query(CryptoPrice).order_by(CryptoPrice.date).all()

def get_price_by_date(db: Session, date_: date, currency: str):
    return db.query(CryptoPrice).filter(
        CryptoPrice.date == date_,
        CryptoPrice.currency == currency
    ).first()

def get_prices_by_currency(db: Session, currency: str):
    return db.query(CryptoPrice).filter(CryptoPrice.currency == currency).order_by(CryptoPrice.date).all()

def create_price(db: Session, price: CryptoPriceCreate):
    db_price = CryptoPrice(**price.dict())
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price

def get_prices_in_date_range(db: Session, currency: str, start: date, end: date):
    return (
        db.query(CryptoPrice)
        .filter(
            CryptoPrice.currency == currency,
            CryptoPrice.date >= start,
            CryptoPrice.date <= end,
        )
        .order_by(CryptoPrice.date)
        .all()
    )