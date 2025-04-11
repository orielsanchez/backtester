import enum
from _typeshed import Incomplete

__all__ = ['_NoValue', '_CopyMode']

class _NoValueType:
    def __new__(cls): ...

_NoValue: Incomplete

class _CopyMode(enum.Enum):
    ALWAYS = True
    NEVER = False
    IF_NEEDED = 2
    def __bool__(self) -> bool: ...
