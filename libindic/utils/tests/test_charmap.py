#!/usr/bin/env python
# -*- coding: utf-8 -*-


from testtools import TestCase

from .. import get_language, char_compare


class GetLanguageTest(TestCase):

    def setUp(self):
        super(GetLanguageTest, self).setUp()

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


class CharMapTest(TestCase):

    def setUp(self):
        super(CharMapTest, self).setUp()

    def test_char_compare(self):
        '''TEST: Character Compare'''
        self.assertEqual(char_compare('a', 'a'), 0)
        self.assertEqual(char_compare(u'ଅ', u'ಅ'), 1)
        self.assertEqual(char_compare(u'ಅ', 'a'), -1)
        self.assertEqual(char_compare(u'ಅ', u'ಅ'), 0)
        self.assertEqual(char_compare('ī', 'iː'), 1)
        self.assertEqual(char_compare('!', ';'), -1)
