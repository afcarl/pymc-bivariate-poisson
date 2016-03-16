import pymc
import numpy as np
import bivariate_poisson_cython

def bivariate_poisson_like(values, l_1, l_2, l_3):
    return  bivariate_poisson_cython.bivariate_poisson_like(values[0],values[1], l_1, l_2, l_3)

def rbivariate_poisson(l_1,l_2,l_3):
    l_1 = max(l_1,eps)
    l_2 = max(l_2,eps)
    l_3 = max(l_3,eps)
    x = pymc.rpoisson(l_3)
    return [pymc.rpoisson(l_1)+x,pymc.rpoisson(l_2)+x]

BivariatePoisson = pymc.stochastic_from_dist('BivariatePoisson', logp = bivariate_poisson_like, random = rbivariate_poisson, dtype=np.int, mv=True)
