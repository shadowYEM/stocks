import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Set page title
st.set_page_config(page_title="Crypto Historical Data")

# Add sidebar title
st.sidebar.title("Crypto Historical Data")

# Add sidebar subtitle
st.sidebar.subheader("Select Currency and Time Frame")

# Add a list of available currencies
selected_currency = st.sidebar.selectbox("Select currency:", ["BTC", "ETH", "XRP", "LTC", "BCH"])

# Add start and end date text inputs
start_date = st.sidebar.text_input("Start date (YYYY-MM-DD):", "2022-01-01")
end_date = st.sidebar.text_input("End date (YYYY-MM-DD):", "2022-12-31")

# Convert start_date and end_date to datetime objects
start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

# Convert datetime objects to timestamps
start_timestamp = int(start_datetime.timestamp())
end_timestamp = int(end_datetime.timestamp())

# Get historical data using cryptocompare API
url = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={selected_currency}&tsym=USD&limit=2000&toTs={end_timestamp}&api_key=c47a0568529639696b2775baa6f1afb21791c5849a7ca8edf33e361c864b2393"
response = requests.get(url)
data = response.json()["Data"]["Data"]

# Clean up the data and convert to pandas DataFrame
df = pd.DataFrame(data)
df["time"] = pd.to_datetime(df["time"], unit="s")
df = df[df["time"] >= start_datetime]
df.set_index("time", inplace=True)

# Show the data using Streamlit
st.title(f"{selected_currency} Historical Data")
st.write(df)

