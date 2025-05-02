from fastapi import APIRouter, Response, Query
from app.db import get_db_session
from app.models.crypto_price import CryptoPrice
import pandas as pd
from datetime import date

router = APIRouter()

def fetch_prices_df(currency: str = None, start: date = None, end: date = None):
    session = get_db_session()
    query = session.query(CryptoPrice)
    if currency:
        query = query.filter(CryptoPrice.currency == currency)
    if start:
        query = query.filter(CryptoPrice.date >= start)
    if end:
        query = query.filter(CryptoPrice.date <= end)
    prices = query.order_by(CryptoPrice.currency, CryptoPrice.date).all()
    session.close()
    df = pd.DataFrame([
        {"date": p.date, "price": p.price, "currency": p.currency}
        for p in prices
    ])
    return df

@router.get("/raw/")
def get_raw_data(
    currency: str = Query(None), start: date = Query(None), end: date = Query(None)
):
    df = fetch_prices_df(currency, start, end)
    return df.to_dict(orient='records')

@router.get("/export/csv/")
def export_csv(
    currency: str = Query(None), start: date = Query(None), end: date = Query(None)
):
    df = fetch_prices_df(currency, start, end)
    csv = df.to_csv(index=False)
    return Response(content=csv, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=crypto_prices.csv"})