from fastapi import APIRouter, Response, Query
from app.routes.data import fetch_prices_df
from app.services.plot import plot_prices
from datetime import date

router = APIRouter()

@router.get("/plot/", response_class=Response, tags=["plot"])
def plot_route(
    coins: list[str] = Query(None),
    start: date = Query(None),
    end: date = Query(None),
    window: int = Query(7)
):
    df = fetch_prices_df(None, start, end)
    img_bytes = plot_prices(df, coins=coins, window=window)
    return Response(content=img_bytes, media_type="image/png")