from distutils.core import setup
from Cython.Build import cythonize

# The “annotate”:True flag creates an interactive HTML view of the Cython code, as a result of the Cython compilation.
# I’ll be using this to check what’s now running at C speeds, and how much code is still running as Python.

ext_options = {"compiler_directives": {"profile": True}, "annotate": True}

setup(ext_modules=cythonize("streaming_tokenizer.pyx", **ext_options))
