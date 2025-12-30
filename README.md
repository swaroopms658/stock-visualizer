# 📈 Golden Cross Visualizer

A data dashboard that allows users to visualize the "Golden Cross" trading strategy on any stock available on Yahoo Finance.

## 🚀 What it does
This tool helps traders visualize market trends by:
1. Fetching real-time historical data using `yfinance`.
2. Calculating 50-day and 200-day Simple Moving Averages (SMA).
3. Plotting interactive Candlestick charts with `plotly` to easily identify crossover points.

## 🛠️ Setup & Running

1. **Install Dependencies:**
   ```bash
   pip install streamlit yfinance pandas plotly pytest