import os
import pandas as pd
import yfinance as yf


def fetch_prices(
    tickers,
    start="2019-01-01",
    end=None,
    interval="1d",
    save=True,
    filename="prices.csv",
):


    raw = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        interval=interval,
        progress=False,
        auto_adjust=True,
    )

    # Extract Close prices
    if isinstance(raw.columns, pd.MultiIndex):
        prices = raw["Close"]
    else:
        prices = raw[["Close"]]
        prices.columns = tickers

    prices = prices.dropna(how="all")

    if save:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        raw_dir = os.path.join(base_dir, "data", "raw")
        os.makedirs(raw_dir, exist_ok=True)

        file_path = os.path.join(raw_dir, filename)
        prices.to_csv(file_path)

        print(f"Saved data to: {file_path}")

    return prices