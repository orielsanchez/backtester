from abc import ABC, abstractmethod

import pandas as pd


class Strategy(ABC):
    """
    Abstract base class for all strategies.
    """

    @abstractmethod
    def generate_positions(self, data: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
        """
        Given price data, return tuple (alpha, beta) where:
        - alpha: Series of stock holdings
        - beta: Series of bond/cash holdings
        """
        pass
