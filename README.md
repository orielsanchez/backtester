# Backtester

A lightweight, modular backtesting engine for simulating and evaluating trading strategies using historical market data. Designed for flexibility and clarity, it supports rapid prototyping and analysis of algorithmic trading ideas.

## Features

- **Strategy Simulation**: Test trading strategies over historical data with customizable logic.
- **Modular Design**: Easily extendable components for strategies, data sources, and execution models.
- **Performance Metrics**: Built-in tools to evaluate strategy performance, including returns, drawdowns, and risk metrics.
- **Data Handling**: Support for various data formats and APIs like Polygon.io.
- **Streamlit App**: Intuitive web interface for running and visualizing backtests.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/orielsanchez/backtester.git
cd backtester
pip install -r requirements.txt
```

Create a `.env` file in the root directory to store your Polygon API key:

```
POLYGON_API_KEY=your_api_key_here
```

## Usage

### Defining a Strategy

Create a strategy by subclassing the `Strategy` base class and implementing the `generate_signals` method:

```python
from backtester.strategies import Strategy

class MyStrategy(Strategy):
    def generate_signals(self, data):
        # Implement logic to generate buy/sell signals
        pass
```

### Running a Backtest

Use the `Backtest` class to run your strategy against historical data:

```python
from backtester import Backtest
from my_strategy import MyStrategy

# Load your historical data
data = load_data('path_to_data.csv')

# Initialize your strategy
strategy = MyStrategy()

# Set up and run the backtest
bt = Backtest(data, strategy)
results = bt.run()

# Analyze results
results.plot()
```

### Running the Streamlit App

Launch the interactive web interface:

```bash
streamlit run app.py
```

This provides a UI for uploading data, selecting strategies, and visualizing results.

## Project Structure

- `backtester/`: Core backtesting engine and components.
  - `strategies/`: Strategy base classes and examples.
  - `data/`: Data loading and preprocessing utilities, including Polygon API support.
  - `execution/`: Order execution models and simulators.
  - `metrics/`: Performance evaluation tools.
- `app.py`: Streamlit frontend for running and displaying backtests.
- `examples/`: TODO: Sample strategies and backtest scripts.
- `tests/`: TODO: Unit tests for core components.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License.
