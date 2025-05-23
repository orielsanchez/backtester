import numpy as np
from _typeshed import Incomplete
from numpy.lib.array_utils import normalize_axis_index as normalize_axis_index
from numpy.random import default_rng as default_rng
from numpy.random._mt19937 import MT19937 as MT19937
from numpy.random._pcg64 import PCG64 as PCG64
from typing import Any, ClassVar, overload

__test__: dict

class Generator:
    _poisson_lam_max: ClassVar[float] = ...
    bit_generator: Incomplete
    def __init__(self, bit_generator) -> Any: ...
    @overload
    def beta(self, a, b, size=...) -> Any: ...
    @overload
    def beta(self, a=..., b=..., size=...) -> Any: ...
    @overload
    def beta(self, a=..., b=..., size=...) -> Any: ...
    @overload
    def beta(self, a=..., b=..., size=...) -> Any: ...
    @overload
    def binomial(self, n, p, size=...) -> Any: ...
    @overload
    def binomial(self, n=..., p=..., size=...) -> Any: ...
    @overload
    def binomial(self, n, p, size=...) -> Any: ...
    def bytes(self, length) -> Any: ...
    def chisquare(self, df, size=...) -> Any: ...
    def choice(self, a, size=..., replace=..., p=..., axis=..., shuffle=...) -> Any: ...
    def dirichlet(self, alpha, size=...) -> Any: ...
    @overload
    def exponential(self, scale=..., size=...) -> Any: ...
    @overload
    def exponential(self, scale=..., size=...) -> Any: ...
    @overload
    def exponential(self, scale=..., size=...) -> Any: ...
    @overload
    def f(self, dfnum, dfden, size=...) -> Any: ...
    @overload
    def f(self, dfnum=..., dfden=..., size=...) -> Any: ...
    @overload
    def gamma(self, shape, scale=..., size=...) -> Any: ...
    @overload
    def gamma(self, shape) -> Any: ...
    @overload
    def geometric(self, p, size=...) -> Any: ...
    @overload
    def geometric(self, p=..., size=...) -> Any: ...
    def gumbel(self, loc=..., scale=..., size=...) -> Any: ...
    def hypergeometric(self, ngood, nbad, nsample, size=...) -> Any: ...
    def integers(self, low, high=..., size=..., dtype=..., endpoint=...) -> Any: ...
    def laplace(self, loc=..., scale=..., size=...) -> Any: ...
    @overload
    def logistic(self, loc=..., scale=..., size=...) -> Any: ...
    @overload
    def logistic(self, x, loc, scale) -> Any: ...
    @overload
    def logistic(self, bins, loc, scale) -> Any: ...
    def lognormal(self, mean=..., sigma=..., size=...) -> Any: ...
    @overload
    def logseries(self, p, size=...) -> Any: ...
    @overload
    def logseries(self, k, p) -> Any: ...
    @overload
    def logseries(self, centres, a) -> Any: ...
    def multinomial(self, n, pvals, size=...) -> Any: ...
    def multivariate_hypergeometric(self, colors, nsample, size=..., 
method=...) -> Any: ...
    def multivariate_normal(self, *args, **kwargs): ...
    def negative_binomial(self, n, p, size=...) -> Any: ...
    def noncentral_chisquare(self, df, nonc, size=...) -> Any: ...
    def noncentral_f(self, dfnum, dfden, nonc, size=...) -> Any: ...
    @overload
    def normal(self, loc=..., scale=..., size=...) -> Any: ...
    @overload
    def normal(self, Gaussian) -> Any: ...
    def pareto(self, a, size=...) -> Any: ...
    @overload
    def permutation(self, x, axis=...) -> Any: ...
    @overload
    def permutation(self, arr) -> Any: ...
    @overload
    def permutation(self, arr, axis=...) -> Any: ...
    @overload
    def permuted(self, x, axis=..., out=...) -> Any: ...
    @overload
    def permuted(self, x, axis=...) -> Any: ...
    @overload
    def permuted(self, x, axis=..., out=...) -> Any: ...
    @overload
    def poisson(self, lam=..., size=...) -> Any: ...
    @overload
    def poisson(self, lam=..., size=...) -> Any: ...
    @overload
    def poisson(self, lam=..., size=...) -> Any: ...
    @overload
    def power(self, a, size=...) -> Any: ...
    @overload
    def power(self, a, samples) -> Any: ...
    @overload
    def random(self, size=..., dtype=..., out=...) -> Any: ...
    @overload
    def random(self) -> Any: ...
    @overload
    def random(self) -> Any: ...
    @overload
    def random(self) -> Any: ...
    def rayleigh(self, scale=..., size=...) -> Any: ...
    @overload
    def shuffle(self, x, axis=...) -> Any: ...
    @overload
    def shuffle(self, arr) -> Any: ...
    @overload
    def shuffle(self, arr) -> Any: ...
    @overload
    def shuffle(self, arr, axis=...) -> Any: ...
    def spawn(self, n_children) -> Any: ...
    def standard_cauchy(self, size=...) -> Any: ...
    def standard_exponential(self, size=..., dtype=..., method=..., out=...) -> Any: ...
    def standard_gamma(self, shape, size=..., dtype=..., out=...) -> Any: ...
    @overload
    def standard_normal(self, size=..., dtype=..., out=...) -> Any: ...
    @overload
    def standard_normal(self, size=...) -> Any: ...
    @overload
    def standard_normal(self) -> Any: ...
    @overload
    def standard_normal(self, size=...) -> Any: ...
    @overload
    def standard_normal(self, size=...) -> Any: ...
    def standard_t(self, df, size=...) -> Any: ...
    def triangular(self, left, mode, right, size=...) -> Any: ...
    def uniform(self, low=..., high=..., size=...) -> Any: ...
    def vonmises(self, mu, kappa, size=...) -> Any: ...
    def wald(self, mean, scale, size=...) -> Any: ...
    @overload
    def weibull(self, a, size=...) -> Any: ...
    @overload
    def weibull(self, x, n, a) -> Any: ...
    @overload
    def zipf(self, a, size=...) -> Any: ...
    @overload
    def zipf(self, a, size=...) -> Any: ...
    def __reduce__(self): ...
