#-*- coding: utf-8 -*-

from silpa_common.langdetect import detect_lang
from silpa_common import servicemethod


def test_langdetect():
    '''TEST: Language Detection'''
    assert detect_lang(u'ನಮಸ್ಕಾರ').values() == ['kn_IN']
    assert detect_lang(u'बॆंगलूरु').values() == ['hi_IN']
    assert detect_lang(u'বাংগ্লা').values() == ['bn_IN']
    assert detect_lang(u'മലയാളം').values() == ['ml_IN']
    assert detect_lang(u'தமிள்').values() == ['ta_IN']
    assert detect_lang(u'తెలుగు').values() == ['te_IN']
    assert detect_lang(u'଒ରିଯା ').values() == ['or_IN']
    assert detect_lang(u'ਪਂਜਾਬਿ').values() == ['pa_IN']
    assert detect_lang(u'ગુજરાતિ').values() == ['gu_IN']
    assert detect_lang("English").values() == ['en_US']


def test_servicemethod():
    '''TEST: Service Method flagging'''
    @servicemethod
    def afun():
        pass

    assert hasattr(afun, 'service_method')
    assert afun.service_method
