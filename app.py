import streamlit as st
import yfinance as yf
import pandas as pd
from vega_datasets import data
import plotly.graph_objects as go
from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention
from datetime import date


# Set page title
# تحديد الكلمات المفتاحية المستهدفة لموقعك
keywords = ["Rasheed Al-qadhi", "Rasheed al qadhi", "project to obtain the stock market data"]

# إنشاء عنوان صفحة موقعك مع تضمين الكلمات المفتاحية
st.title("Hello, I'm RASHEED AL-QADHI. This is a project to obtain the stock market data .")

# إنشاء محتوى الصفحة مع تضمين الكلمات المفتاحية
st.write("Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes. The software libraries used in the project are streamlit , yfinance, pandas, vega_datasets, plotly, streamlit_extras")


# colored_header(
#     label="Hi , i'm RASHEED AL-QADHI ",
#     description="",
#     color_name="orange-70",
# )

# Set up social media icons
with st.container():
    col1, col2, col3 = st.columns(3)
    col1.markdown("[![Twitter](https://img.shields.io/twitter/follow/shadowYEM?style=social)](https://twitter.com/shadowYEM)")
    col2.markdown("[![GitHub](https://img.shields.io/github/followers/shadowYEM?style=social)](https://github.com/shadowYEM)")
    col3.markdown("[![Telegram](https://img.shields.io/badge/-Telegram-white?color=white&logo=telegram&logoColor=blue)](https://t.me/ShadowYE)")
    # col4.markdown("[![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&color=white&logo=kaggle&logoColor=blue)](https://kaggle.com/shadowYE)")


colored_header(
    label="A project containing 20 stock exchange shares",
    description="",
    color_name="orange-70",
)



st.sidebar.title('Stock Data :part_alternation_mark:')

# Set page title

# Define the user inputs
tickers = st.sidebar.selectbox('Select Tickers', ['AAPL','MSFT', 'AMZN', 'GOOGL', 'META', 'TSLA', 'BRK.A', 'BRK.B', 
                                                  'NVDA', 'JPM', 'JNJ', 'V', 'PG', 'DIS','INTC', 'PFE', 'KO', 'XOM', 'MCD', 'IBM' ], index=0,  format_func=lambda x: x.upper())
today = date.today()

start_date = st.sidebar.date_input('Start date', value=pd.to_datetime('2022-03-22'))
end_date = st.sidebar.date_input('End date', value=today)

# Fetch stock data from Yahoo
data = yf.download(tickers, start=start_date, end=end_date)

# Display stock data
st.header(f'Stock data for :red[{tickers}]')
st.dataframe(data, width=1000)


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


@st.cache_resource
def convert_df(df):
    st.title(f'Data :red[{tickers}] Download ')
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(data)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name=f'{tickers}.csv',
    mime='text/csv',
)

