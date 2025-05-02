from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import time

COINS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "XMR": "monero",
}

# Scrape historical daily prices for the last 30 days from CoinGecko
# CoinGecko URL: https://www.coingecko.com/en/coins/{coin}/historical_data?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD#panel

def scrape_coin_history(coin_symbol):
    coin_id = COINS[coin_symbol]
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=29)
    url = f"https://www.coingecko.com/en/coins/{coin_id}/historical_data?start_date={start_date}&end_date={end_date}#panel"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch data for {coin_symbol}")
    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.find("table", class_="table")
    if not table:
        raise Exception(f"No data table found for {coin_symbol}")
    rows = table.find_all("tr")[1:]  # skip header
    records = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 2:
            continue
        date_str = cols[0].text.strip()
        price_str = cols[1].text.strip().replace("$", "").replace(",", "")
        try:
            price = float(price_str)
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            records.append({
                "date": date_obj,
                "price": price,
                "currency": coin_symbol,
            })
        except Exception:
            continue
    time.sleep(1)  # be polite to the server
    return records

def scrape_all_coins():
    all_records = []
    for symbol in COINS:
        try:
            all_records.extend(scrape_coin_history(symbol))
        except Exception as e:
            print(f"Error scraping {symbol}: {e}")
    return all_records

def get_supported_coins():
    return [{"symbol": k, "name": v} for k, v in COINS.items()]