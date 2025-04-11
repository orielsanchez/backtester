import os
from datetime import datetime

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from data_loader import fetch_data_polygon
from engine import BacktestEngine
from metrics import summarize_performance
from moving_average import MovingAverageCrossStrategy
from plotting import plot_drawdowns, plot_equity_curve, plot_price_with_trades

load_dotenv()

api_key = os.getenv("POLYGON_API_KEY")
if api_key is None:
    raise RuntimeError("POLYGON_API_KEY not found in .env")


st.set_page_config(layout="wide")
st.title("📊 Backtest Dashboard")

# ─────────────────────────────────────────────────────────────
# Sidebar: Data Input
st.sidebar.header("Data Input")
data_source = st.sidebar.radio("Select data source:", ["Upload CSV", "Use polygon.io"])

data = None

if data_source == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        try:
            data = (
                pd.read_csv(uploaded_file, parse_dates=["Date"])
                .set_index("Date")
                .sort_index()
            )
            st.sidebar.success("CSV loaded.")
        except Exception:
            st.sidebar.error("Error reading CSV. Ensure it has a 'Date' column.")
    else:
        st.sidebar.info("Using sample AAPL data.")
        data = (
            pd.read_csv("data/AAPL.csv", parse_dates=["Date"])
            .set_index("Date")
            .sort_index()
        )

else:
    ticker = st.sidebar.text_input("Ticker Symbol", value="AAPL")
    start_date = st.sidebar.date_input("Start Date", value=datetime(2024, 1, 1))
    end_date = st.sidebar.date_input("End Date", value=datetime(2025, 1, 1))

    if ticker and start_date < end_date:
        fetched = fetch_data_polygon(ticker, str(start_date), str(end_date), api_key)
        if not fetched.empty:
            data = fetched
            st.sidebar.success(f"Loaded {ticker} from polygon.io")
        else:
            st.sidebar.warning(f"No data returned for {ticker}")
    else:
        st.sidebar.warning("Enter valid dates.")

# ─────────────────────────────────────────────────────────────
# Strategy settings
st.sidebar.header("Strategy Settings")
short_window = st.sidebar.number_input("Short Window", 5, 100, value=20)
long_window = st.sidebar.number_input("Long Window", 10, 200, value=50)

# Backtest settings
st.sidebar.header("Backtest Settings")
slippage = st.sidebar.slider("Slippage (%)", 0.0, 1.0, 0.1) / 100
tx_cost = st.sidebar.slider("Transaction Cost (%)", 0.0, 1.0, 0.1) / 100

# ─────────────────────────────────────────────────────────────
# Run backtest and display results
if data is not None and not data.empty:
    strategy = MovingAverageCrossStrategy(short_window, long_window)
    engine = BacktestEngine(
        strategy, data, slippage_pct=slippage, transaction_cost_pct=tx_cost
    )
    equity_curve = engine.run()
    performance = summarize_performance(equity_curve)

    st.subheader("📈 Price with Trades")
    plot_price_with_trades(data, engine.trade_log)

    st.subheader("💰 Equity Curve")
    plot_equity_curve(equity_curve)

    st.subheader("📉 Drawdowns")
    plot_drawdowns(equity_curve)

    st.subheader("📋 Performance Metrics")
    st.write({k: f"{v:.2%}" for k, v in performance.items()})
else:
    st.warning("No data available. Please upload a file or fetch using polygon.")
