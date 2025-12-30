import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- Configuration ---
st.set_page_config(page_title="Golden Cross Visualizer", layout="wide")

# --- Helper Functions ---
@st.cache_data
def fetch_stock_data(ticker, start_date, end_date):
    """Fetches historical data from Yahoo Finance."""
    try:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        if data.empty:
            return None
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def calculate_metrics(df):
    """Calculates Simple Moving Averages (SMA)."""
    # Ensure we are working with a flat structure if MultiIndex is returned
    if isinstance(df.columns, pd.MultiIndex):
        df = df.xs(df.columns[0][1], axis=1, level=1)
        
    df['SMA50'] = df['Close'].rolling(window=50).mean()
    df['SMA200'] = df['Close'].rolling(window=200).mean()
    return df

# --- UI Layout ---
st.title("📈 Golden Cross Strategy Visualizer")
st.markdown("""
This tool visualizes the **Golden Cross** (Bullish) and **Death Cross** (Bearish) technical patterns.
* **Golden Cross:** When the 50-day SMA crosses *above* the 200-day SMA.
* **Death Cross:** When the 50-day SMA crosses *below* the 200-day SMA.
""")

# Sidebar Inputs
st.sidebar.header("Configuration")
ticker = st.sidebar.text_input("Stock Ticker", value="AAPL").upper()
years_back = st.sidebar.slider("Years of Data", 1, 10, 3)

# Date Calculation
end_date = datetime.today()
start_date = end_date - timedelta(days=years_back*365)

# --- Execution ---
if ticker:
    with st.spinner(f"Loading data for {ticker}..."):
        raw_data = fetch_stock_data(ticker, start_date, end_date)
    
    if raw_data is not None:
        processed_data = calculate_metrics(raw_data)
        
        # Key Metrics Display
        last_price = processed_data['Close'].iloc[-1]
        sma_50 = processed_data['SMA50'].iloc[-1]
        sma_200 = processed_data['SMA200'].iloc[-1]
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"${last_price:.2f}")
        col2.metric("50-Day SMA", f"${sma_50:.2f}", delta_color="normal")
        col3.metric("200-Day SMA", f"${sma_200:.2f}", delta_color="normal")

        # --- Plotting with Plotly ---
        fig = go.Figure()

        # Candlestick
        fig.add_trace(go.Candlestick(
            x=processed_data.index,
            open=processed_data['Open'],
            high=processed_data['High'],
            low=processed_data['Low'],
            close=processed_data['Close'],
            name='Price'
        ))

        # SMA Lines
        fig.add_trace(go.Scatter(x=processed_data.index, y=processed_data['SMA50'], 
                                 line=dict(color='orange', width=2), name='SMA 50'))
        fig.add_trace(go.Scatter(x=processed_data.index, y=processed_data['SMA200'], 
                                 line=dict(color='blue', width=2), name='SMA 200'))

        fig.update_layout(title=f"{ticker} Price vs Moving Averages", xaxis_title="Date", yaxis_title="Price", height=600)
        st.plotly_chart(fig, use_container_width=True)

        st.write("### Raw Data (Last 5 Days)")
        st.dataframe(processed_data.tail())

    else:
        st.error("No data found. Please check the Ticker symbol.")