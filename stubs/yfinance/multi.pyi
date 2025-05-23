import pandas as _pd
from . import Ticker as Ticker, shared as shared, utils as utils
from .data import YfData as YfData
from _typeshed import Incomplete

def download(tickers, start: Incomplete | None = None, end: Incomplete | None = None, actions: bool = False, threads: bool = True, ignore_tz: Incomplete | None = None, group_by: str = 'column', auto_adjust: Incomplete | None = None, back_adjust: bool = False, repair: bool = False, keepna: bool = False, progress: bool = True, period: str = 'max', interval: str = '1d', prepost: bool = False, proxy: Incomplete | None = None, rounding: bool = False, timeout: int = 10, session: Incomplete | None = None, multi_level_index: bool = True) -> _pd.DataFrame | None: ...
