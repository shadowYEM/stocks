import streamlit as st
import yfinance as yf
import pandas as pd
from vega_datasets import data
import plotly.graph_objects as go

st.sidebar.title('Yahoo Stock Data :part_alternation_mark:')

# Set page title

# Define the user inputs
tickers = st.sidebar.selectbox('Select Tickers', ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA', 'NFLX'], index=0,  format_func=lambda x: x.upper())
start_date = st.sidebar.date_input('Start date', value=pd.to_datetime('2022-03-22'))
end_date = st.sidebar.date_input('End date', value=pd.to_datetime('2023-03-21'))

# Fetch stock data from Yahoo
data = yf.download(tickers, start=start_date, end=end_date)

# Display stock data
st.header(f'Stock data for :red[{tickers}]')
st.write(data)


st.title('Data visualization :zap:')

# Set up plotly figure
fig = go.Figure()



# Add candlestick trace for stock prices
fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'],
                             name="Stock Prices"))

# Add moving average trace for 50-day period
fig.add_trace(go.Scatter(x=data.index,
                         y=data['Close'],
                         mode='lines',
                         name='Moving Average (50 days)'))

# Add plotly layout
fig.update_layout(title=f"{tickers} Stock Prices",
                  xaxis_title="Date",
                  yaxis_title="Price (USD)")

# Render plotly figure using streamlit
st.plotly_chart(fig)

# Add download button to download data
