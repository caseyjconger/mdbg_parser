import unittest

from mdbg_entry import MdbgEntry

class MdbgEntryTestCase(unittest.TestCase):
    """Unit test for MdbgEntry class.
    """
    def setUp(self):
        self.MDBG_PATH = '/home/casey/zhongwen/cedict_1_0_ts_utf-8_mdbg.txt'
        with open(self.MDBG_PATH, 'r') as reader:
            self.raw = reader.readlines()
        self.mdbg = []
        for num, entry in enumerate(self.raw[1500:1600]):
            mdbg_entry = MdbgEntry(entry)
            entry = mdbg_entry.entry.update({'index' : num})
            self.mdbg.append(mdbg_entry)

    def test_tone_is_numerical(self):
        for entry in self.mdbg[1500:1600]:
            self.assertIsInstance(entry.pinyin['tone'], int)

#    def test_num_chars_pinyin(self):
#        for entry in self.mdbg:



if __name__ == '__main__':
    unittest.main()

