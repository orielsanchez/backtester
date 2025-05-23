from ._isocbind import isoc_kindmap as isoc_kindmap
from .auxfuncs import getfortranname as getfortranname, isexternal as isexternal, isfunction as isfunction, isfunction_wrap as isfunction_wrap, isintent_in as isintent_in, isintent_out as isintent_out, islogicalfunction as islogicalfunction, ismoduleroutine as ismoduleroutine, isscalar as isscalar, issubroutine as issubroutine, issubroutine_wrap as issubroutine_wrap, outmess as outmess, show as show
from _typeshed import Incomplete

def var2fixfortran(vars, a, fa: Incomplete | None = None, f90mode: Incomplete | None = None): ...
def useiso_c_binding(rout): ...
def createfuncwrapper(rout, signature: int = 0): ...
def createsubrwrapper(rout, signature: int = 0): ...
def assubr(rout): ...
