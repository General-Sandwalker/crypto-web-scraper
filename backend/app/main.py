from fastapi import FastAPI
from app.models.crypto_price import Base
from app.db import engine
from app.routes import (
    scraper_router,
    data_router,
    plot_router,
)
from app.routes.coins import router as coins_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Crypto Analytics API",
    description="REST API for scraping, storing, and visualizing Bitcoin, Ethereum, and Monero prices.",
    version="0.2.0",
)

app.include_router(scraper_router)
app.include_router(data_router)
app.include_router(plot_router)
app.include_router(coins_router)