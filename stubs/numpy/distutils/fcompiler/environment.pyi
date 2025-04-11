from _typeshed import Incomplete

__metaclass__ = type

class EnvironmentConfig:
    def __init__(self, distutils_section: str = 'ALL', **kw) -> None: ...
    def dump_variable(self, name): ...
    def dump_variables(self) -> None: ...
    def __getattr__(self, name): ...
    def get(self, name, default: Incomplete | None = None): ...
    def clone(self, hook_handler): ...
    def use_distribution(self, dist) -> None: ...
