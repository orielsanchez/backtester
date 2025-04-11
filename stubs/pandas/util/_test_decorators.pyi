import pytest
from _typeshed import Incomplete
from pandas._config import get_option as get_option
from pandas._typing import F as F
from pandas.compat import IS64 as IS64, is_platform_windows as is_platform_windows
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from typing import Callable

def skip_if_installed(package: str) -> pytest.MarkDecorator: ...
def skip_if_no(package: str, min_version: str | None = None) -> pytest.MarkDecorator: ...

skip_if_32bit: Incomplete
skip_if_windows: Incomplete
skip_if_not_us_locale: Incomplete

def parametrize_fixture_doc(*args) -> Callable[[F], F]: ...
def mark_array_manager_not_yet_implemented(request) -> None: ...

skip_array_manager_not_yet_implemented: Incomplete
skip_array_manager_invalid_test: Incomplete
skip_copy_on_write_not_yet_implemented: Incomplete
skip_copy_on_write_invalid_test: Incomplete
