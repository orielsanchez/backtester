from ..utils import dynamic_docstring as dynamic_docstring, generate_list_table_from_dict_universal as generate_list_table_from_dict_universal
from .query import EquityQuery as EquityQuery, FundQuery as FundQuery, QueryBase as QueryBase
from _typeshed import Incomplete
from yfinance.data import YfData as YfData

PREDEFINED_SCREENER_BODY_DEFAULTS: Incomplete
PREDEFINED_SCREENER_QUERIES: Incomplete

def screen(query: str | EquityQuery | FundQuery, offset: int = None, size: int = None, sortField: str = None, sortAsc: bool = None, userId: str = None, userIdType: str = None, session: Incomplete | None = None, proxy: Incomplete | None = None): ...
