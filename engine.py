from dataclasses import dataclass

import pandas as pd

from strategy_base import Strategy


@dataclass
class Trade:
    timestamp: pd.Timestamp
    action: str
    price: float
    quantity: float
    cash_after_trade: float


class BacktestEngine:
    strategy: Strategy
    data: pd.DataFrame
    slippage_pct: float
    transaction_cost_pct: float
    equity_curve: pd.Series
    trade_log: list[Trade]

    def __init__(
        self,
        strategy: Strategy,
        data: pd.DataFrame,
        slippage_pct: float = 0.0,
        transaction_cost_pct: float = 0.0,
    ) -> None:
        self.strategy = strategy
        self.data = data
        self.slippage_pct = slippage_pct
        self.transaction_cost_pct = transaction_cost_pct
        self.equity_curve: pd.Series = pd.Series(dtype="float64")
        self.trade_log: list[Trade] = []

    def run(self) -> pd.Series:
        alpha, beta = self.strategy.generate_positions(self.data)
        prices = self.data["Close"]
        portfolio_value = pd.Series(index=self.data.index, dtype="float64")

        prev_position = 0.0
        current_cash = beta.iloc[0]  # Track cash manually for cost deductions

        for t in self.data.index:
            price = prices.loc[t]
            position = alpha.loc[t]

            # Check for trade
            if position != prev_position:
                action = "BUY" if position > prev_position else "SELL"
                quantity = abs(position - prev_position)

                # Apply slippage (worse price)
                effective_price = (
                    price * (1 + self.slippage_pct)
                    if action == "BUY"
                    else price * (1 - self.slippage_pct)
                )

                # Total trade value
                trade_value = quantity * effective_price

                # Apply transaction cost
                cost = trade_value * self.transaction_cost_pct

                # Adjust cash for trade + cost
                if action == "BUY":
                    current_cash -= trade_value + cost
                else:
                    current_cash += trade_value - cost

                self.trade_log.append(
                    Trade(t, action, effective_price, quantity, current_cash)
                )
                prev_position = position

            # Calculate portfolio value at time t
            portfolio_value.loc[t] = position * price + current_cash

        self.equity_curve = portfolio_value
        return self.equity_curve
