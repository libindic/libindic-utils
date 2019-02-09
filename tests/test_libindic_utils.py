#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from libindic.utils import detect_lang, servicemethod, char_compare, get_language


class LangDetectTest(unittest.TestCase):

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

    def test_char_compare(self):
        '''TEST: Character Compare'''
        self.assertEqual(char_compare('a', 'a'), 0)
        self.assertEqual(char_compare(u'ଅ', u'ಅ'), 1)
        self.assertEqual(char_compare(u'ಅ', 'a'), -1)
        self.assertEqual(char_compare(u'ಅ', u'ಅ'), 0)
        self.assertEqual(char_compare('ī', 'iː'), 1)
        self.assertEqual(char_compare('!', ';'), -1)

    def test_servicemethod(self):
        '''TEST: Service Method flagging'''
        @servicemethod
        def afun():
            pass

        assert hasattr(afun, 'service_method')
        assert afun.service_method

    def test_get_language(self):
        '''TEST: Get language'''
        self.assertEqual(get_language(u'ನ'), 'kn_IN')
        self.assertEqual(get_language(u'അ'), 'ml_IN')
        self.assertEqual(get_language(u'அ'), 'ta_IN')
        self.assertEqual(get_language(u'అ'), 'te_IN')
        self.assertEqual(get_language(u'અ'), 'gu_IN')
        self.assertEqual(get_language(u'অ'), 'bn_IN')
        self.assertEqual(get_language(u'ਅ'), 'pa_IN')
        self.assertEqual(get_language(u'अ'), 'hi_IN')
        self.assertEqual(get_language(u'ଅ'), 'or_IN')
        self.assertEqual(get_language('a'), 'en_US')
        self.assertEqual(get_language('eː'), 'IPA')
        self.assertEqual(get_language('ê'), 'ISO15919')
        self.assertEqual(get_language('!'), None)


if __name__ == '__main__':
    unittest.main()