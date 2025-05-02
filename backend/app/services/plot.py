import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd

def plot_prices(df: pd.DataFrame, coins=None, window=7):
    df['date'] = pd.to_datetime(df['date'])
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = {"BTC": "#f7931a", "ETH": "#3c3c3d", "XMR": "#ff6600"}
    if coins is None:
        coins = df['currency'].unique()
    for coin in coins:
        coin_df = df[df['currency'] == coin]
        ax.plot(
            coin_df['date'],
            coin_df['price'],
            label=coin,
            color=colors.get(coin, None),
            alpha=0.7,
        )
        # Rolling mean
        if len(coin_df) >= window:
            ax.plot(
                coin_df['date'],
                coin_df['price'].rolling(window=window, min_periods=1).mean(),
                label=f"{coin} {window}d mean",
                linestyle='--',
                color=colors.get(coin, None),
                alpha=0.5,
            )
    ax.set_title("Crypto Price Comparison")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()