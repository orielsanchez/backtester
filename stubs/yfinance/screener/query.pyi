import abc
import numbers
from ..utils import dynamic_docstring as dynamic_docstring, generate_list_table_from_dict_universal as generate_list_table_from_dict_universal
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import TypeVar
from yfinance.const import EQUITY_SCREENER_EQ_MAP as EQUITY_SCREENER_EQ_MAP, EQUITY_SCREENER_FIELDS as EQUITY_SCREENER_FIELDS, FUND_SCREENER_EQ_MAP as FUND_SCREENER_EQ_MAP, FUND_SCREENER_FIELDS as FUND_SCREENER_FIELDS
from yfinance.exceptions import YFNotImplementedError as YFNotImplementedError

T = TypeVar('T', bound=str | numbers.Real)

class QueryBase(ABC, metaclass=abc.ABCMeta):
    operator: Incomplete
    operands: Incomplete
    def __init__(self, operator: str, operand: list['QueryBase'] | tuple[str, tuple[str | numbers.Real, ...]]) -> None: ...
    @property
    @abstractmethod
    def valid_fields(self) -> list: ...
    @property
    @abstractmethod
    def valid_values(self) -> dict: ...
    def to_dict(self) -> dict: ...

class EquityQuery(QueryBase):
    @property
    def valid_fields(self) -> dict: ...
    @property
    def valid_values(self) -> dict: ...

class FundQuery(QueryBase):
    @property
    def valid_fields(self) -> dict: ...
    @property
    def valid_values(self) -> dict: ...
