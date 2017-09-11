#!/usr/bin/python
# -*- coding: utf-8 -*-


from testtools import TestCase

from .. import detect_lang, servicemethod


class LangDetectTest(TestCase):

    def setUp(self):
        super(LangDetectTest, self).setUp()

    def test_langdetect(self):
        '''TEST: Language Detection'''
        self.assertEqual(detect_lang(u'ನಮಸ್ಕಾರ')[u'ನಮಸ್ಕಾರ'], 'kn_IN')
        self.assertEqual(detect_lang(u'बॆंगलूरु')[u'बॆंगलूरु'], 'hi_IN')
        self.assertEqual(detect_lang(u'বাংগ্লা')[u'বাংগ্লা'], 'bn_IN')
        self.assertEqual(detect_lang(u'മലയാളം')[u'മലയാളം'], 'ml_IN')
        self.assertEqual(detect_lang(u'தமிள்')[u'தமிள்'], 'ta_IN')
        self.assertEqual(detect_lang(u'తెలుగు')[u'తెలుగు'], 'te_IN')
        self.assertEqual(detect_lang(u'଒ରିଯା')[u'଒ରିଯା'], 'or_IN')
        self.assertEqual(detect_lang(u'ਪਂਜਾਬਿ')[u'ਪਂਜਾਬਿ'], 'pa_IN')
        self.assertEqual(detect_lang(u'ગુજરાતિ')[u'ગુજરાતિ'], 'gu_IN')
        self.assertEqual(detect_lang("English")["English"], 'en_US')


def test_servicemethod():
    '''TEST: Service Method flagging'''
    @servicemethod
    def afun():
        pass

    assert hasattr(afun, 'service_method')
    assert afun.service_method
