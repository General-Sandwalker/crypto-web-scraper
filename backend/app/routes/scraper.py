from fastapi import APIRouter
from app.services.scraper import scrape_all_coins
from app.models.crypto_price import CryptoPrice
from app.db import get_db_session

router = APIRouter()

@router.post("/scrape/", tags=["scraper"])
def scrape_and_save():
    records = scrape_all_coins()
    session = get_db_session()
    inserted = 0
    for rec in records:
        if not session.query(CryptoPrice).filter_by(date=rec["date"], currency=rec["currency"]).first():
            session.add(CryptoPrice(**rec))
            inserted += 1
    session.commit()
    session.close()
    return {"inserted": inserted, "total_fetched": len(records)}