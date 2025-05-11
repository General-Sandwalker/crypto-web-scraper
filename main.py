import os
import asyncio
import pandas as pd
import requests
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

import matplotlib.pyplot as plt

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/cryptodb")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Scraper function (using CoinGecko public API)
def fetch_crypto_prices(symbols=["ethereum"]):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(symbols),
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch prices")
    data = response.json()
    prices = []
    for symbol in symbols:
        prices.append({
            "symbol": symbol,
            "price": data[symbol]["usd"],
            "timestamp": datetime.utcnow()
        })
    return prices

# Save prices to DB
def save_prices_to_db(prices):
    db = SessionLocal()
    for price in prices:
        db_price = CryptoPrice(**price)
        db.add(db_price)
    db.commit()
    db.close()

# Pandas data processing and plotting
def plot_prices():
    db = SessionLocal()
    query = db.query(CryptoPrice).all()
    db.close()
    if not query:
        raise Exception("No data to plot")
    df = pd.DataFrame([{
        "symbol": q.symbol,
        "price": q.price,
        "timestamp": q.timestamp
    } for q in query])
    plt.figure(figsize=(10, 6))
    for symbol in df["symbol"].unique():
        df_symbol = df[df["symbol"] == symbol]
        plt.plot(df_symbol["timestamp"], df_symbol["price"], label=symbol)
    plt.xlabel("Timestamp")
    plt.ylabel("Price (USD)")
    plt.title("Crypto Prices Over Time")
    plt.legend()
    plt.tight_layout()
    img_path = "crypto_prices.png"
    plt.savefig(img_path)
    plt.close()
    return img_path

@app.post("/scrape")
def scrape_and_save():
    try:
        prices = fetch_crypto_prices()
        save_prices_to_db(prices)
        return {"status": "success", "data": prices}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/plot")
def get_plot():
    try:
        img_path = plot_prices()
        return {"status": "success", "plot_image": img_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/prices")
def get_prices():
    db = SessionLocal()
    prices = db.query(CryptoPrice).order_by(CryptoPrice.timestamp.desc()).limit(100).all()
    db.close()
    return [
        {
            "symbol": p.symbol,
            "price": p.price,
            "timestamp": p.timestamp.isoformat()
        } for p in prices
    ]


