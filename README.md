# LibIndic Utilities


[![Build Status](https://travis-ci.org/libindic/silpa_common.svg?branch=master)](https://travis-ci.org/libindic/silpa_common)
[![Coverage Status](https://coveralls.io/repos/github/libindic/silpa_common/badge.svg?branch=master)](https://coveralls.io/github/libindic/silpa_common?branch=master)


This package provides common functions needed by LibIndic web application
itself and modules which are hosted by LibIndic. There are 2 submodules
provided by this package

* charmap - provides character mapping for Indic and other languages
* langdetect - module provides language detecting capabilities
* Also provides a decorator servicemethod, this should be used by
  modules which want to expose their methods via JSONRPC modules

## Installation
1. Clone the repository `git clone https://github.com/libindic/silpa_common.git`
2. Change to the cloned directory `cd silpa_common`
3. Run setup.py to create installable source `python setup.py sdist`
4. Install using pip `pip install dist/libindic-utils*.tar.gz`

## Usage
```
>>> from libindic.utils import langdetect
>>> from libindic.utils import charmap
```
