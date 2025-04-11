import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from engine import Trade


def plot_price_with_trades(data: pd.DataFrame, trades: list[Trade]) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data["Close"], label="Price", alpha=0.8)

    for trade in trades:
        color = "green" if trade.action == "BUY" else "red"
        marker = "^" if trade.action == "BUY" else "v"
        ax.scatter(
            trade.timestamp,
            trade.price,
            color=color,
            marker=marker,
            label=trade.action,
        )

    ax.set_title("Price with Trades")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.grid(True)

    # Avoid duplicate legend entries
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())

    st.pyplot(fig)


def plot_equity_curve(equity_curve: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(equity_curve, label="Equity Curve", color="blue")
    ax.set_title("Portfolio Value Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Equity ($)")
    ax.grid(True)
    st.pyplot(fig)


def plot_drawdowns(equity_curve: pd.Series) -> None:
    rolling_max = equity_curve.cummax()
    drawdown = equity_curve / rolling_max - 1

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.fill_between(drawdown.index, drawdown, 0, color="red", alpha=0.3)
    ax.set_title("Drawdowns")
    ax.set_xlabel("Date")
    ax.set_ylabel("Drawdown (%)")
    ax.grid(True)
    st.pyplot(fig)
