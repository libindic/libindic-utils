#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Language Detection based on unicode range
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import string


def check(old_lang_code, new_lang_code):
    """
    this function helps to make sure that every letter
    of a word have same language.
    if language codes for every letter are same
    then it returns True.
    """

    if(old_lang_code == ''):
        return True
    else:
        if(old_lang_code != new_lang_code):
            return False
        else:
            return True

"""
error when word contains letters from
more then one languages
"""
mix_error_line = "mixing of more then one language found"


def detect_lang(text):
    """
    Detect the language of the given text using the unicode range.
    This function can take a chunk of text and return a dictionary
    containing word-language key-value pairs.
    """

    words = text.split(" ")
    word_count = len(words)
    word_iter = 0
    word = ""
    result_dict = dict()
    while word_iter < word_count:
        word = words[word_iter]
        if(word):
            orig_word = word
            #remove the punctuations
            for punct in string.punctuation:
                word = word.replace(punct, " ")
            length = len(word)
            index = 0

            # detected language code, initially blank
            # one argument for `function : check()`
            lang_code = ''

            # scan left to write, skip any punctuations,
            # the detection stops in the first match itself.
            while index < length:
                letter = word[index]
                if not letter.isalpha():
                    index = index + 1
                    continue

                if ((ord(letter) >= 0x0D00) & (ord(letter) <= 0x0D7F)):
                    if(check(lang_code, "ml_IN")):
                        result_dict[orig_word] = "ml_IN"
                        lang_code = "ml_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((ord(letter) >= 0x0980) & (ord(letter) <= 0x09FF)):
                    if(check(lang_code, "bn_IN")):
                        result_dict[orig_word] = "bn_IN"
                        lang_code = "bn_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((ord(letter) >= 0x0900) & (ord(letter) <= 0x097F)):
                    if(check(lang_code, "hi_IN")):
                        result_dict[orig_word] = "hi_IN"
                        lang_code = "hi_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((ord(letter) >= 0x0A80) & (ord(letter) <= 0x0AFF)):
                    if(check(lang_code, "gu_IN")):
                        result_dict[orig_word] = "gu_IN"
                        lang_code = "gu_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((ord(letter) >= 0x0A00) & (ord(letter) <= 0x0A7F)):
                    if(check(lang_code, "pa_IN")):
                        result_dict[orig_word] = "pa_IN"
                        lang_code = "pa_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((ord(letter) >= 0x0C80) & (ord(letter) <= 0x0CFF)):
                    if(check(lang_code, "kn_IN")):
                        result_dict[orig_word] = "kn_IN"
                        lang_code = "kn_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((ord(letter) >= 0x0B00) & (ord(letter) <= 0x0B7F)):
                    if(check(lang_code, "or_IN")):
                        result_dict[orig_word] = "or_IN"
                        lang_code = "or_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((ord(letter) >= 0x0B80) & (ord(letter) <= 0x0BFF)):
                    if(check(lang_code, "ta_IN")):
                        result_dict[orig_word] = "ta_IN"
                        lang_code = "ta_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((ord(letter) >= 0x0C00) & (ord(letter) <= 0x0C7F)):
                    if(check(lang_code, "te_IN")):
                        result_dict[orig_word] = "te_IN"
                        lang_code = "te_IN"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                if ((letter <= u'z')):  # this is fallback case.
                    if(check(lang_code, "en_US")):
                        result_dict[orig_word] = "en_US"
                        lang_code = "en_US"
                        index = index + 1
                        continue
                    else:
                        result_dict[orig_word] = mix_error_line
                        break

                index = index + 1
        word_iter = word_iter + 1
    return result_dict
