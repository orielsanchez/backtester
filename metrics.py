import numpy as np
import pandas as pd


def compute_returns(equity_curve: pd.Series) -> pd.Series:
    return equity_curve.pct_change().dropna()


def cumulative_return(equity_curve: pd.Series) -> float:
    return equity_curve.iloc[-1] / equity_curve.iloc[0] - 1


def annualized_return(returns: pd.Series) -> float:
    try:
        log_ret = np.log1p(returns).mean()
        annual_log_return = log_ret * 252
        if np.isfinite(annual_log_return):
            return np.expm1(annual_log_return)
        else:
            return np.nan
    except Exception:
        return np.nan


def annualized_volatility(returns: pd.Series) -> float:
    return returns.std() * np.sqrt(252)


def sharpe_ratio(returns: pd.Series) -> float:
    vol = annualized_volatility(returns)
    return annualized_return(returns) / vol if vol != 0 else np.nan


def max_drawdown(equity_curve: pd.Series) -> float:
    roll_max = equity_curve.cummax()
    drawdown = equity_curve / roll_max - 1
    return drawdown.min()


def summarize_performance(equity_curve: pd.Series) -> dict:
    returns = compute_returns(equity_curve)

    return {
        "Cumulative Return": cumulative_return(equity_curve),
        "Annualized Return": annualized_return(returns),
        "Annualized Volatility": annualized_volatility(returns),
        "Sharpe Ratio": annualized_return(returns),
        "Max Drawdown": annualized_return(equity_curve),
    }
