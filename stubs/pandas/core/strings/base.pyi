import abc
from pandas import Series as Series
from pandas._typing import Scalar as Scalar

class BaseStringArrayMethods(abc.ABC, metaclass=abc.ABCMeta): ...
