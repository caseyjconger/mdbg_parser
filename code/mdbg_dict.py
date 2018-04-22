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
    def __init__(self,
                 mdbg_raw_path='../data/cedict_1_0_ts_utf-8_mdbg.txt',
                 from_json=True,
                 mdbg_src_json_path='../data/MDBG.json',
                 verbose=True):
        """
        Constructor for MDBG object
        """
        self.RAW_PATH = mdbg_raw_path 
        self.SRC_JSON_PATH = mdbg_src_json_path
        self._from_json = from_json
        self._verbose = verbose

        self.mdbg_dict = {}
        self.header = []
        self.entries = []
        self.mdbg_entries = []
        self.raw = ''

        if self._from_json:  # Use a preprocessed JSON file to build dictionary
            if self._verbose:
                print('Loading MDBG from {}'.format(self.SRC_JSON_PATH))
            with open(self.SRC_JSON_PATH, 'r') as reader:
                self.json_in = json.load(reader)
            self.mdbg_dict = self.json_in
            self.header = self.mdbg_dict['header']
            self.entries = self.mdbg_dict['entries']
            if self._verbose:
                print('Loading of MDBG from JSON complete')
        else:                                        # Parse raw MDBG text file
            with open(self.RAW_PATH, 'r') as reader:
                self.raw = reader.readlines()
                self.mdbg_entries = [
                    MdbgEntry(l) for l in self.raw if l[0] != '#'
                ]
                self.entries = [en.entry for en in self.mdbg_entries]
                self.header = [ln for ln in self.raw if ln[0] == '#']

    ###########################################################################
    # I/O                                                                     #
    ###########################################################################
    def write_to_json(self, save_path='../data/MDBG.json', verbose=True):
        """
        Writes parsed mdbg dictionary to json file
        """
        self.json = {
            'header': self.header,
            'entries': self.entries
        }
        if verbose:
            print('Writing parsed MDBG to {}'.format(save_path))
        with open(save_path, 'w') as writer:
            json.dump(self.json, writer, indent=4)
        if verbose:
            print('Writing to JSON complete')
        return self.json

    ############################################################################
    # WORD FREQUENCIES                                                         #
    ############################################################################
    def get_freq(self, word):
        this_word = word
        import nltk
        from nltk.corpus import sinica_treebank

        corpus = sinica_treebank.words()
        from collections import Counter
        freq_list = Counter(corpus)
        print(freq_list)



###############################################################################
# MAIN                                                                        #
###############################################################################
if __name__ == '__main__':
    mdbg = MDBG(from_json=True)
    mdbg.get_freq('')
#    entries = [xx.entry for xx in mdbg.entries]
#    with open('test_dict.json', 'w') as outfile:
#        json.dump(entries, outfile, indent=4)
