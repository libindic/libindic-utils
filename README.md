Common functions for SILPA
==========================

This package provides common functions needed by SILPA web application
itself and modules which are hosted by SILPA. There are 2 submodules
provided by this package

* charmap - provides character mapping for Indic and other languages
* langdetect - module provides language detecting capabilities
* Also provides a decorator servicemethod, this should be used by
  modules which want to expose their methods via JSONRPC modules
