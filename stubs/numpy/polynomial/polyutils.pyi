__all__ = ['as_series', 'trimseq', 'trimcoef', 'getdomain', 'mapdomain', 'mapparms', 'format_float']

def trimseq(seq): ...
def as_series(alist, trim: bool = True): ...
def trimcoef(c, tol: int = 0): ...
def getdomain(x): ...
def mapparms(old, new): ...
def mapdomain(x, old, new): ...
def format_float(x, parens: bool = False): ...
