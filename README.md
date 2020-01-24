# streaming_word_tokenizer


GOALS
-----

The goal of this project is to tokenize text without having to read all of the text
into memory. The projects aims to do this very efficiently with a target goal of
1GB/minute on a 2020 MacBook Pro class of machine.

The project uses streaming layers, the base layer emits token class objects that
can be combined into n-grams if needed. This, the base layer, can be used in a
program as a library given a sequence of source text files, or can be used in a
CLI environment where the result will be displayed on stdout one token object per
line.

LICENSE
-------

New BSD. See LICENSE

FUTURE
------

  - Evaluate performance improvements using cython
  - TBD

EXAMPLE
-------

DEPENDENCIES
------------

Supports Python 3.4+. It is pure Python and requires no dependencies beyond the
standard library.

RELATED PROJECTS:

  - `TextBlob <https://github.com/sloria/TextBlob>`__`
