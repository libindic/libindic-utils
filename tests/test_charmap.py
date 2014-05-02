# -*- coding: utf-8 -*-

from silpa_common.charmap import get_language, char_compare


def test_get_language():
    '''TEST: Get language'''
    assert get_language(u'ನ') == 'kn_IN'
    assert get_language(u'അ') == 'ml_IN'
    assert get_language(u'அ') == 'ta_IN'
    assert get_language(u'అ') == 'te_IN'
    assert get_language(u'અ') == 'gu_IN'
    assert get_language(u'অ') == 'bn_IN'
    assert get_language(u'ਅ') == 'pa_IN'
    assert get_language(u'अ') == 'hi_IN'
    assert get_language(u'ଅ') == 'or_IN'
    assert get_language('a') == 'en_US'
    assert get_language('eː') == 'IPA'
    assert get_language('ê') == 'ISO15919'
    assert get_language('!') is None


def test_char_compare():
    '''TEST: Character Compare'''
    assert char_compare('a', 'a') == 0
    assert char_compare(u'ଅ', u'ಅ') == 1
    assert char_compare(u'ಅ', 'a') == -1
    assert char_compare(u'ಅ', u'ಅ') == 0
    assert char_compare('ī', 'iː') == 1
    assert char_compare('!', ';') == -1
