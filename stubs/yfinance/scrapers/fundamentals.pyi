import pandas as pd
from _typeshed import Incomplete
from yfinance import const as const, utils as utils
from yfinance.data import YfData as YfData
from yfinance.exceptions import YFException as YFException, YFNotImplementedError as YFNotImplementedError

class Fundamentals:
    proxy: Incomplete
    def __init__(self, data: YfData, symbol: str, proxy: Incomplete | None = None) -> None: ...
    @property
    def financials(self) -> Financials: ...
    @property
    def earnings(self) -> dict: ...
    @property
    def shares(self) -> pd.DataFrame: ...

class Financials:
    def __init__(self, data: YfData, symbol: str) -> None: ...
    def get_income_time_series(self, freq: str = 'yearly', proxy: Incomplete | None = None) -> pd.DataFrame: ...
    def get_balance_sheet_time_series(self, freq: str = 'yearly', proxy: Incomplete | None = None) -> pd.DataFrame: ...
    def get_cash_flow_time_series(self, freq: str = 'yearly', proxy: Incomplete | None = None) -> pd.DataFrame: ...
    def get_financials_time_series(self, timescale, keys: list, proxy: Incomplete | None = None) -> pd.DataFrame: ...
