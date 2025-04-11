from .npy_pkg_config import *
from . import __config__ as __config__, ccompiler as ccompiler, unixccompiler as unixccompiler
from _typeshed import Incomplete
from numpy._pytesttester import PytestTester as PytestTester

test: Incomplete

def customized_fcompiler(plat: Incomplete | None = None, compiler: Incomplete | None = None): ...
def customized_ccompiler(plat: Incomplete | None = None, compiler: Incomplete | None = None, verbose: int = 1): ...
