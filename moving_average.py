import pandas as pd

from strategy_base import Strategy


class MovingAverageCrossStrategy(Strategy):
    short_window: int
    long_window: int
    initial_capital: float

    def __init__(
        self, short_window: int = 20, long_window: int = 50, capital: float = 100_000
    ):
        self.short_window = short_window
        self.long_window = long_window
        self.initial_capital = capital

    def generate_positions(self, data: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
        # Compute short and long moving averages
        short_ma = data["Close"].rolling(window=self.short_window).mean()
        long_ma = data["Close"].rolling(window=self.long_window).mean()

        # Generate raw trading signals: 1 = buy, -1 = sell, 0 = hold
        signals = pd.Series(0, index=data.index)
        signals[short_ma > long_ma] = 1
        signals[short_ma < long_ma] = -1

        # Initialize alpha (stock holdings) and beta (cash holdings) as time-indexed series
        alpha = pd.Series(0.0, index=data.index)
        cash = pd.Series(self.initial_capital, index=data.index)

        # Initialize current state variables
        current_position = 0.0  # Number of shares held
        current_cash = self.initial_capital  # Amount of cash currently held

        # Iterate through each time point to simulate trades
        for t in data.index:
            price = float(data["Close"].loc[t])  # ensure raw float
            signal = signals.loc[t]

            if signal == 1 and current_cash >= price:
                # Buy signal: use all available cash to buy as many whole shares as possible
                current_position = current_cash / price
                current_cash = 0.0

            elif signal == -1:
                # Sell signal: liquidate all shares
                current_cash += current_position * price
                current_position = 0.0

            # Record portfolio state at time t
            alpha.loc[t] = current_position  # alpha(t): float, can be fractional
            cash.loc[t] = current_cash  # beta(t): cash held

        return alpha, cash
