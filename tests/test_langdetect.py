#!/usr/bin/python
# -*- coding: utf-8 -*-


from silpa_common.langdetect import detect_lang
from silpa_common import servicemethod


def test_langdetect():
    '''TEST: Language Detection'''
    assert detect_lang(u'ನಮಸ್ಕಾರ')[u'ನಮಸ್ಕಾರ'] == 'kn_IN'
    assert detect_lang(u'बॆंगलूरु')[u'बॆंगलूरु'] == 'hi_IN'
    assert detect_lang(u'বাংগ্লা')[u'বাংগ্লা'] == 'bn_IN'
    assert detect_lang(u'മലയാളം')[u'മലയാളം'] == 'ml_IN'
    assert detect_lang(u'தமிள்')[u'தமிள்'] == 'ta_IN'
    assert detect_lang(u'తెలుగు')[u'తెలుగు'] == 'te_IN'
    assert detect_lang(u'଒ରିଯା')[u'଒ରିଯା'] == 'or_IN'
    assert detect_lang(u'ਪਂਜਾਬਿ')[u'ਪਂਜਾਬਿ'] == 'pa_IN'
    assert detect_lang(u'ગુજરાતિ')[u'ગુજરાતિ'] == 'gu_IN'
    assert detect_lang("English")["English"] == 'en_US'


def test_servicemethod():
    '''TEST: Service Method flagging'''
    @servicemethod
    def afun():
        pass

    assert hasattr(afun, 'service_method')
    assert afun.service_method
