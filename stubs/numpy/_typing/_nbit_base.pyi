from .._utils import set_module as set_module

class NBitBase:
    def __init_subclass__(cls) -> None: ...

class _256Bit(NBitBase): ...
class _128Bit(_256Bit): ...
class _96Bit(_128Bit): ...
class _80Bit(_96Bit): ...
class _64Bit(_80Bit): ...
class _32Bit(_64Bit): ...
class _16Bit(_32Bit): ...
class _8Bit(_16Bit): ...
