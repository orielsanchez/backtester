from . import polyutils as pu
from ._polybase import ABCPolyBase
from _typeshed import Incomplete

__all__ = ['legzero', 'legone', 'legx', 'legdomain', 'legline', 'legadd', 'legsub', 'legmulx', 'legmul', 'legdiv', 'legpow', 'legval', 'legder', 'legint', 'leg2poly', 'poly2leg', 'legfromroots', 'legvander', 'legfit', 'legtrim', 'legroots', 'Legendre', 'legval2d', 'legval3d', 'leggrid2d', 'leggrid3d', 'legvander2d', 'legvander3d', 'legcompanion', 'leggauss', 'legweight']

legtrim = pu.trimcoef

def poly2leg(pol): ...
def leg2poly(c): ...

legdomain: Incomplete
legzero: Incomplete
legone: Incomplete
legx: Incomplete

def legline(off, scl): ...
def legfromroots(roots): ...
def legadd(c1, c2): ...
def legsub(c1, c2): ...
def legmulx(c): ...
def legmul(c1, c2): ...
def legdiv(c1, c2): ...
def legpow(c, pow, maxpower: int = 16): ...
def legder(c, m: int = 1, scl: int = 1, axis: int = 0): ...
def legint(c, m: int = 1, k=[], lbnd: int = 0, scl: int = 1, axis: int = 0): ...
def legval(x, c, tensor: bool = True): ...
def legval2d(x, y, c): ...
def leggrid2d(x, y, c): ...
def legval3d(x, y, z, c): ...
def leggrid3d(x, y, z, c): ...
def legvander(x, deg): ...
def legvander2d(x, y, deg): ...
def legvander3d(x, y, z, deg): ...
def legfit(x, y, deg, rcond: Incomplete | None = None, full: bool = False, w: Incomplete | None = None): ...
def legcompanion(c): ...
def legroots(c): ...
def leggauss(deg): ...
def legweight(x): ...

class Legendre(ABCPolyBase):
    domain: Incomplete
    window: Incomplete
    basis_name: str
