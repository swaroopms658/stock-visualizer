# 📈 Golden Cross Stock Visualizer

A data-driven dashboard that visualizes the "Golden Cross" and "Death Cross" technical trading patterns using real-time market data.

## 📖 The Challenge
**Goal:** Build an interesting data tool using the `yfinance` library.
**My Approach:** I built an interactive web application that helps traders visualize moving averages to identify potential bullish or bearish market trends without manual calculation.

## 🚀 Features
* **Real-time Data:** Fetches up-to-the-minute stock history from Yahoo Finance.
* **Interactive Charts:** Uses Plotly to render zoomable candlestick charts.
* **Dynamic Analysis:** Calculates 50-day and 200-day Simple Moving Averages (SMA) on the fly.
* **Customizable:** Users can select any ticker symbol (AAPL, TSLA, NVDA, etc.) and lookback period.

## 🛠️ How to Run It

### Option 1: GitHub Codespaces (Cloud - Recommended)
1.  Open this repository in GitHub Codespaces.
2.  In the terminal, install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    streamlit run app.py
    ```
4.  Click **"Open in Browser"** when the notification appears.

### Option 2: Locally (Your Computer)
1.  Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd stock-visualizer
    ```
2.  Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app:
    ```bash
    streamlit run app.py
    ```

## 🧪 Running Tests
This project includes automated tests to verify the accuracy of the Moving Average calculations.
To run the tests:
```bash
pytest tests.py
