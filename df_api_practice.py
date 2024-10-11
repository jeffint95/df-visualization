import requests
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch data from Alpha Vantage
def fetch_stock_data(symbol):
    api_key = 'your_api_key'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full'
    response = requests.get(url)
    data = response.json()
    
    # Convert the JSON data to a pandas DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    return df

# Fetch and plot data for Apple (AAPL)
stock_data = fetch_stock_data('AAPL')
stock_data['Close'].plot(title='AAPL Stock Price', figsize=(10,5))
plt.show()

import plotly.graph_objects as go

def plot_candlestick(df, stock):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                     open=df['Open'],
                     high=df['High'],
                     low=df['Low'],
                     close=df['Close'])])
    fig.update_layout(title=f'{stock} Stock Candlestick Chart', 
                      xaxis_title='Date',
                      yaxis_title='Price (USD)')
    fig.show()

# Plot candlestick chart for AAPL
plot_candlestick(stock_data, 'AAPL')
