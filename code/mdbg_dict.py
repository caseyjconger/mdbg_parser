from mdbg_entry import MdbgEntry

import json

###############################################################################
###############################################################################
# MDBG Dictionary                                                             #
###############################################################################
###############################################################################


class MDBG(object):
    """Represents a parsing of the mdbg dictionary
       https://www.mdbg.net/chinese/dictionary?page=cc-cedict
    """

    ###########################################################################
    # Constructor                                                             #
    ###########################################################################
    def __init__(self):
        self.MDBG_PATH = '/home/casey/zhongwen/cedict_1_0_ts_utf-8_mdbg.txt'
        with open(self.MDBG_PATH, 'r') as reader:
            self.raw = reader.readlines()
            self.mdbg_entries = [MdbgEntry(ln) for ln in self.raw if ln[0] != '#']
            self.entries = [en.entry for en in self.mdbg_entries]
            self.header= [MdbgEntry(ln) for ln in self.raw if ln[0] == '#']

    ###########################################################################
    # I/O                                                                     #
    ###########################################################################
    def write_to_json(self, filename='MDBG.json'):
        """
        Writes parsed mdbg dictionaty to json file
        """
        self.json = {
            'header' : self.header,
            'entries' : self.entries,
        }
        return self.json


if __name__ == '__main__':
    mdbg = MDBG()
    print(mdbg.write_to_json())
#    entries = [xx.entry for xx in mdbg.entries]
#    with open('test_dict.json', 'w') as outfile:
#        json.dump(entries, outfile, indent=4)
