# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the extension module
ext_module = Extension(
    "hello_wrapper",
    sources=["hello_wrapper.pyx"],
    include_dirs=["."]  # Include current directory for hello.h
)

# Setup configuration
setup(
    name="hello_world_example",
    ext_modules=cythonize([ext_module])
)