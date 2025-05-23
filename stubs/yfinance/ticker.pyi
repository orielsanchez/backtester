import pandas as _pd
from .base import TickerBase as TickerBase
from .scrapers.funds import FundsData as FundsData
from _typeshed import Incomplete

class Ticker(TickerBase):
    def __init__(self, ticker, session: Incomplete | None = None, proxy: Incomplete | None = None) -> None: ...
    def option_chain(self, date: Incomplete | None = None, tz: Incomplete | None = None): ...
    @property
    def isin(self): ...
    @property
    def major_holders(self) -> _pd.DataFrame: ...
    @property
    def institutional_holders(self) -> _pd.DataFrame: ...
    @property
    def mutualfund_holders(self) -> _pd.DataFrame: ...
    @property
    def insider_purchases(self) -> _pd.DataFrame: ...
    @property
    def insider_transactions(self) -> _pd.DataFrame: ...
    @property
    def insider_roster_holders(self) -> _pd.DataFrame: ...
    @property
    def dividends(self) -> _pd.Series: ...
    @property
    def capital_gains(self) -> _pd.Series: ...
    @property
    def splits(self) -> _pd.Series: ...
    @property
    def actions(self) -> _pd.DataFrame: ...
    @property
    def shares(self) -> _pd.DataFrame: ...
    @property
    def info(self) -> dict: ...
    @property
    def fast_info(self): ...
    @property
    def calendar(self) -> dict: ...
    @property
    def sec_filings(self) -> dict: ...
    @property
    def recommendations(self): ...
    @property
    def recommendations_summary(self): ...
    @property
    def upgrades_downgrades(self): ...
    @property
    def earnings(self) -> _pd.DataFrame: ...
    @property
    def quarterly_earnings(self) -> _pd.DataFrame: ...
    @property
    def income_stmt(self) -> _pd.DataFrame: ...
    @property
    def quarterly_income_stmt(self) -> _pd.DataFrame: ...
    @property
    def ttm_income_stmt(self) -> _pd.DataFrame: ...
    @property
    def incomestmt(self) -> _pd.DataFrame: ...
    @property
    def quarterly_incomestmt(self) -> _pd.DataFrame: ...
    @property
    def ttm_incomestmt(self) -> _pd.DataFrame: ...
    @property
    def financials(self) -> _pd.DataFrame: ...
    @property
    def quarterly_financials(self) -> _pd.DataFrame: ...
    @property
    def ttm_financials(self) -> _pd.DataFrame: ...
    @property
    def balance_sheet(self) -> _pd.DataFrame: ...
    @property
    def quarterly_balance_sheet(self) -> _pd.DataFrame: ...
    @property
    def balancesheet(self) -> _pd.DataFrame: ...
    @property
    def quarterly_balancesheet(self) -> _pd.DataFrame: ...
    @property
    def cash_flow(self) -> _pd.DataFrame: ...
    @property
    def quarterly_cash_flow(self) -> _pd.DataFrame: ...
    @property
    def ttm_cash_flow(self) -> _pd.DataFrame: ...
    @property
    def cashflow(self) -> _pd.DataFrame: ...
    @property
    def quarterly_cashflow(self) -> _pd.DataFrame: ...
    @property
    def ttm_cashflow(self) -> _pd.DataFrame: ...
    @property
    def analyst_price_targets(self) -> dict: ...
    @property
    def earnings_estimate(self) -> _pd.DataFrame: ...
    @property
    def revenue_estimate(self) -> _pd.DataFrame: ...
    @property
    def earnings_history(self) -> _pd.DataFrame: ...
    @property
    def eps_trend(self) -> _pd.DataFrame: ...
    @property
    def eps_revisions(self) -> _pd.DataFrame: ...
    @property
    def growth_estimates(self) -> _pd.DataFrame: ...
    @property
    def sustainability(self) -> _pd.DataFrame: ...
    @property
    def options(self) -> tuple: ...
    @property
    def news(self) -> list: ...
    @property
    def earnings_dates(self) -> _pd.DataFrame: ...
    @property
    def history_metadata(self) -> dict: ...
    @property
    def funds_data(self) -> FundsData: ...
