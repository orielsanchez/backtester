import warnings
from collections.abc import Generator
from pandas.compat import PY311 as PY311
from typing import Literal

def assert_produces_warning(expected_warning: type[Warning] | bool | tuple[type[Warning], ...] | None = ..., filter_level: Literal['error', 'ignore', 'always', 'default', 'module', 'once'] = 'always', check_stacklevel: bool = True, raise_on_extra_warnings: bool = True, match: str | None = None) -> Generator[list[warnings.WarningMessage], None, None]: ...
def maybe_produces_warning(warning: type[Warning], condition: bool, **kwargs): ...
