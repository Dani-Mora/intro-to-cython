from distutils.core import setup
from Cython.Build import cythonize

import numpy

setup(
    ext_modules=cythonize(
        "sort.pyx",
        compiler_directives={"language_level": "3"},
        annotate=True,
    ),
    include_dirs=[numpy.get_include()],
)
