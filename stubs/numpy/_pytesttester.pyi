from _typeshed import Incomplete

__all__ = ['PytestTester']

class PytestTester:
    module_name: Incomplete
    __module__: Incomplete
    def __init__(self, module_name) -> None: ...
    def __call__(self, label: str = 'fast', verbose: int = 1, extra_argv: Incomplete | None = None, doctests: bool = False, coverage: bool = False, durations: int = -1, tests: Incomplete | None = None): ...
