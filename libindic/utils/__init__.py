# -*- coding: utf-8 -*-

from .langdetect import detect_lang
from .charmap import char_compare, get_language, charmap, charmap_transphon

__all__ = ['servicemethod']


def servicemethod(fn):
    fn.service_method = True
    return fn
