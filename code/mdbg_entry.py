import sys
import numpy as np
import json
import unittest

###############################################################################
###############################################################################
# MDBG_entry                                                                  #
###############################################################################
###############################################################################
class MdbgEntry(object):
    """Encapsulates a single entry in the MDBG dictionary.
    """

    ###########################################################################
    # Constructor                                                             #
    ###########################################################################
    def __init__(self, entry):
        self.raw_entry = entry
        self.chars, _rest = self._split_chars_rest(self.raw_entry)
        self.trad, self.simp = self._split_trad_simp(self.chars)
        self.pinyin, _defs = self._split_pinyin_defs(_rest)
        self.defs = self._split_definitions(_defs)
        self.entry = {
            'simplified' : self.simp,
            'traditional' : self.trad,
            'pinyin' : self.pinyin,
            'definitions' : self.defs,
        }

    ###########################################################################
    # Helper Functions                                                        #
    ###########################################################################
    def _split_chars_rest(self, entry):
        """Split entry into character piece and everything else.
        """
        chars_rest = entry.split('[')
        chars = chars_rest[0].strip()
        rest = chars_rest[1:]
        rest = '[' + '['.join(rest)
        return chars, rest

    def _split_pinyin_defs(self, rest):
        pinyin_defs = rest.split('/')
        pinyin = pinyin_defs[0]
        defs = '/' +  '/'.join(pinyin_defs[1:])

        pinyin = pinyin.split('[')[1].split(']')[0]
        pinyin = pinyin.split(' ')
        pinyin = [self._parse_pinyin(pp) for pp in pinyin]
        return pinyin, defs

    def _split_definitions(self, defs):
        defs = defs.split('/')
        drop = ['', '\n']
        defs[:] = [xx for xx in defs if xx not in drop]
        return defs

    def _split_trad_simp(self, chars):
        trad_simp = chars.split(' ')
        trad = trad_simp[0]
        simp = trad_simp[1:]
        simp = ''.join(simp)
        return trad, simp

    def _parse_pinyin(self, pinyin):
        tone = pinyin[-1]
        syll = pinyin[:-1].lower()
        syll_len = len(syll)
        pinyin_dict = {
            'raw' : pinyin,
            'syllable' : syll,
            'length' : syll_len,
            'tone' : tone,
        }
        return pinyin_dict

    def get_info(self):
        self.num_simp_chars = len(self.simp)
        self.num_trad_chars = len(self.trad)
        self.num_pinyin_sylls = len(self.pinyin)
#        print(self.num_simp_chars, self.num_trad_chars, self.num_pinyin_sylls)
        #TODO: Test for consistent lengths





if __name__ == '__main__':
    MDBG_PATH = '/home/casey/zhongwen/cedict_1_0_ts_utf-8_mdbg.txt'
    with open(MDBG_PATH, 'r') as reader:
        raw = reader.readlines()
    for entry in raw[1500:1600]:
        mdbg_entry = MdbgEntry(entry)
        print(json.dumps(mdbg_entry.entry, indent=4))
        print(mdbg_entry.get_info())
#    unittest.main()


#class MDBG(object):
#    """Represents a parsing of the mdbg dictionary
#       https://www.mdbg.net/chinese/dictionary?page=cc-cedict
#    """
#
#
#    def __init__(self):
#        self.MDBG_PATH = '/home/casey/zhongwen/cedict_1_0_ts_utf-8_mdbg.txt'
#        with open(self.MDBG_PATH, 'r') as reader:
#            self.raw = np.array(reader.readlines())
#
#
#
#
#class MDBG_TEST(unittest.TestCase):
#    """Unit test class for MDBG class.
#    """
#
#    def setUp(self):
#        self.mdbg = MDBG()
#        self.rand_entry = self.mdbg.raw[1569]
#        self.chars, self.rest = self.mdbg._split_chars_rest(self.rand_entry)
#
#    def test_chars_rest_split(self):
#        self.assertEqual(len(self.rest), 2)
#
#
#
#
#if __name__ == '__main__':
##    unittest.main()
#    mdbg = MDBG()
#    test_entry = mdbg.raw[1569:1579]
#    for entry in test_entry:
#        print(json.dumps(mdbg._split_entry(entry), indent=4))
#
