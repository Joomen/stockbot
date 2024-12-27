import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def get_data(tickers,start_date,end_date):
    data ={}
    for ticker in tickers:
        try:
            df = pd.read_csv(f"./data/{ticker}.csv",index_col=0,parse_dates=True)
            data[ticker] = df
        except Exception as e:
            print(f"Error:{e}")

            df = yf.download(ticker,start=start_date,end=end_date)

if __name__ == "__main__":
    tickers = ["AAPL","MSFT","GOOG"]
    start_date = "2019-01-01"
    end_date = "2021-01-01"
