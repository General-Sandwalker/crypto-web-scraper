from fastapi import APIRouter
from app.services.scraper import get_supported_coins

router = APIRouter()

@router.get("/coins/", tags=["coins"])
def list_coins():
    return get_supported_coins()
