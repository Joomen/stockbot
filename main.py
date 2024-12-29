import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def get_data(tickers,start_date,end_date):
    data ={}
    for ticker in tickers:
        try:
            df = pd.read_csv(f"./data/{ticker}.csv",index_col=0,parse_dates=['Date'],
                             date_parser= lambda x:pd.to_datetime(x,format='%Y-%m-%d'))
            data[ticker] = df
        except Exception as e:
            print(f"Error:{e}")

            df = yf.download(ticker,start=start_date,end=end_date)
            data[ticker] = df
            df.to_csv(f"./data/{ticker}.csv")
    return data

def plot_data(data,ticker):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index, open=data["Open"],
                                 high=data['High'],low=data['Low'],close=data['Close'],name="Price"))
    fig.update_layout(
        title=f"{ticker} Stock Analysis",
        xaxis_title="Date",
        yaxis_title="Price",
    xaxis=dict(rangeslider=dict(visible=False)))
    fig.show()

def plot_with_strategy(data,ticker):
    fig = go.Figure()
    fig = make_subplots(rows=2,cols=1,shared_xaxes=True,
                        vertical_spacing=0.02,row_width=[0.7,0.3])

if __name__ == "__main__":
    tickers = ["AAPL","MSFT","GOOG"]
    start_date = "2019-01-01"
    end_date = "2021-01-01"
    stock_data = get_data(tickers,start_date,end_date)
    for ticker,data in stock_data.items():
        print(ticker)
        plot_data(data,ticker)