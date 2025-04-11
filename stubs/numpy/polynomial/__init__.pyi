from .chebyshev import Chebyshev as Chebyshev
from .hermite import Hermite as Hermite
from .hermite_e import HermiteE as HermiteE
from .laguerre import Laguerre as Laguerre
from .legendre import Legendre as Legendre
from .polynomial import Polynomial as Polynomial

__all__ = ['set_default_printstyle', 'polynomial', 'Polynomial', 'chebyshev', 'Chebyshev', 'legendre', 'Legendre', 'hermite', 'Hermite', 'hermite_e', 'HermiteE', 'laguerre', 'Laguerre']

def set_default_printstyle(style) -> None: ...

# Names in __all__ with no definition:
#   chebyshev
#   hermite
#   hermite_e
#   laguerre
#   legendre
#   polynomial
