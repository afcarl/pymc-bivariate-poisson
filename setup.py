from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("bivpois/bivariate_poisson_cython.pyx"),
)
