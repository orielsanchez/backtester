from _typeshed import Incomplete
from collections.abc import Mapping
from pandas._libs.properties import cache_readonly as cache_readonly
from pandas._typing import F, T
from typing import Any, Callable

__all__ = ['Appender', 'cache_readonly', 'deprecate', 'deprecate_kwarg', 'deprecate_nonkeyword_arguments', 'doc', 'future_version_msg', 'Substitution']

def deprecate(name: str, alternative: Callable[..., Any], version: str, alt_name: str | None = None, klass: type[Warning] | None = None, stacklevel: int = 2, msg: str | None = None) -> Callable[[F], F]: ...
def deprecate_kwarg(old_arg_name: str, new_arg_name: str | None, mapping: Mapping[Any, Any] | Callable[[Any], Any] | None = None, stacklevel: int = 2) -> Callable[[F], F]: ...
def future_version_msg(version: str | None) -> str: ...
def deprecate_nonkeyword_arguments(version: str | None, allowed_args: list[str] | None = None, name: str | None = None) -> Callable[[F], F]: ...
def doc(*docstrings: None | str | Callable, **params) -> Callable[[F], F]: ...

class Substitution:
    params: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, func: F) -> F: ...
    def update(self, *args, **kwargs) -> None: ...

class Appender:
    addendum: str | None
    join: Incomplete
    def __init__(self, addendum: str | None, join: str = '', indents: int = 0) -> None: ...
    def __call__(self, func: T) -> T: ...
