from ..data import YfData as YfData, utils as utils
from _typeshed import Incomplete

class Market:
    market: Incomplete
    session: Incomplete
    proxy: Incomplete
    timeout: Incomplete
    def __init__(self, market: str, session: Incomplete | None = None, proxy: Incomplete | None = None, timeout: int = 30) -> None: ...
    @property
    def status(self): ...
    @property
    def summary(self): ...
