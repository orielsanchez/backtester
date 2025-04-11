from . import polyutils as pu
from ._polybase import ABCPolyBase
from _typeshed import Incomplete

__all__ = ['lagzero', 'lagone', 'lagx', 'lagdomain', 'lagline', 'lagadd', 'lagsub', 'lagmulx', 'lagmul', 'lagdiv', 'lagpow', 'lagval', 'lagder', 'lagint', 'lag2poly', 'poly2lag', 'lagfromroots', 'lagvander', 'lagfit', 'lagtrim', 'lagroots', 'Laguerre', 'lagval2d', 'lagval3d', 'laggrid2d', 'laggrid3d', 'lagvander2d', 'lagvander3d', 'lagcompanion', 'laggauss', 'lagweight']

lagtrim = pu.trimcoef

def poly2lag(pol): ...
def lag2poly(c): ...

lagdomain: Incomplete
lagzero: Incomplete
lagone: Incomplete
lagx: Incomplete

def lagline(off, scl): ...
def lagfromroots(roots): ...
def lagadd(c1, c2): ...
def lagsub(c1, c2): ...
def lagmulx(c): ...
def lagmul(c1, c2): ...
def lagdiv(c1, c2): ...
def lagpow(c, pow, maxpower: int = 16): ...
def lagder(c, m: int = 1, scl: int = 1, axis: int = 0): ...
def lagint(c, m: int = 1, k=[], lbnd: int = 0, scl: int = 1, axis: int = 0): ...
def lagval(x, c, tensor: bool = True): ...
def lagval2d(x, y, c): ...
def laggrid2d(x, y, c): ...
def lagval3d(x, y, z, c): ...
def laggrid3d(x, y, z, c): ...
def lagvander(x, deg): ...
def lagvander2d(x, y, deg): ...
def lagvander3d(x, y, z, deg): ...
def lagfit(x, y, deg, rcond: Incomplete | None = None, full: bool = False, w: Incomplete | None = None): ...
def lagcompanion(c): ...
def lagroots(c): ...
def laggauss(deg): ...
def lagweight(x): ...

class Laguerre(ABCPolyBase):
    domain: Incomplete
    window: Incomplete
    basis_name: str
