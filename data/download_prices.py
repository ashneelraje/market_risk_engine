import yfinance as yf
import pandas as pd

def download_prices(ticker, start_date, end_date):
    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False
    )

    if isinstance(df.columns, pd.MultiIndex):
        prices = df.loc[:, ("Adj Close", ticker)]

    else:
        prices = df["Adj Close"]

    prices.columns.name = "Ticker"
    return prices
