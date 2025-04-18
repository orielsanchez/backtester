import pandas as pd
from _typeshed import Incomplete
from yfinance import utils as utils
from yfinance.const import quote_summary_valid_modules as quote_summary_valid_modules
from yfinance.data import YfData as YfData
from yfinance.exceptions import YFDataException as YFDataException, YFException as YFException

info_retired_keys_price: Incomplete
info_retired_keys_exchange: Incomplete
info_retired_keys_marketCap: Incomplete
info_retired_keys_symbol: Incomplete
info_retired_keys = info_retired_keys_price | info_retired_keys_exchange | info_retired_keys_marketCap | info_retired_keys_symbol

class FastInfo:
    proxy: Incomplete
    def __init__(self, tickerBaseObject, proxy: Incomplete | None = None) -> None: ...
    def keys(self): ...
    def items(self): ...
    def values(self): ...
    def get(self, key, default: Incomplete | None = None): ...
    def __getitem__(self, k): ...
    def __contains__(self, k) -> bool: ...
    def __iter__(self): ...
    def toJSON(self, indent: int = 4): ...
    @property
    def currency(self): ...
    @property
    def quote_type(self): ...
    @property
    def exchange(self): ...
    @property
    def timezone(self): ...
    @property
    def shares(self): ...
    @property
    def last_price(self): ...
    @property
    def previous_close(self): ...
    @property
    def regular_market_previous_close(self): ...
    @property
    def open(self): ...
    @property
    def day_high(self): ...
    @property
    def day_low(self): ...
    @property
    def last_volume(self): ...
    @property
    def fifty_day_average(self): ...
    @property
    def two_hundred_day_average(self): ...
    @property
    def ten_day_average_volume(self): ...
    @property
    def three_month_average_volume(self): ...
    @property
    def year_high(self): ...
    @property
    def year_low(self): ...
    @property
    def year_change(self): ...
    @property
    def market_cap(self): ...

class Quote:
    proxy: Incomplete
    def __init__(self, data: YfData, symbol: str, proxy: Incomplete | None = None) -> None: ...
    @property
    def info(self) -> dict: ...
    @property
    def sustainability(self) -> pd.DataFrame: ...
    @property
    def recommendations(self) -> pd.DataFrame: ...
    @property
    def upgrades_downgrades(self) -> pd.DataFrame: ...
    @property
    def calendar(self) -> dict: ...
    @property
    def sec_filings(self) -> dict: ...
    @staticmethod
    def valid_modules(): ...
