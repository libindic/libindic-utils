LibIndic Utilities
==================

.. image:: https://img.shields.io/pypi/v/libindic-utils.svg
    :target: https://pypi.python.org/pypi/libindic-utils
    :alt: PyPI Version

This package provides common functions needed by LibIndic web application
itself and modules which are hosted by `LibIndic`_. There are 2 submodules
provided by this package

* charmap - provides character mapping for Indic and other languages
* langdetect - module provides language detecting capabilities
* Also provides a decorator servicemethod, this should be used by
  modules which want to expose their methods via JSONRPC modules

Installation
------------

Python 3 is required. Using with `venv`_ is recommended

  .. code-block:: console

    $ pip install libindic-utils

Usage
-----

  .. code-block:: python

    from libindic.utils import get_language
    get_language(u'অ') # 'bn_IN'

.. _`LibIndic`: https://libindic.org
.. _`venv`: https://docs.python.org/3/library/venv.html