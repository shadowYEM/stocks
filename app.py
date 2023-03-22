import streamlit as st
import pandas as pd
import yfinance as yf

# Set page title
st.set_page_config(page_title="Cryptocurrency Data", page_icon=":money_with_wings:")

# Set sidebar options
st.sidebar.title("Select Cryptocurrency and Date Range")
crypto = st.sidebar.selectbox("Select Cryptocurrency", ["BTC-USD", "ETH-USD", "LTC-USD"])
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Get cryptocurrency data from Yahoo Finance API
crypto_data = yf.download(crypto, start=start_date, end=end_date)

# Display cryptocurrency data in table format
st.write(f"## {crypto} Data from {start_date} to {end_date}")
st.write(crypto_data)
