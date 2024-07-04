import unittest
from collections import Counter
import sys
sys.path.append("src")
from transformation import get_words


class TestTransformation(unittest.TestCase):

    # test words extraction
    def test_get_words(self):
        text = "MPs should attend all debates, not merely turn up and vote or strike pairing deals. With other commitments, a five day Commons is not workable for MPs: I suggest three full days (9am to 6pm minimum), with one or two days for Committees, leaving at least one day for constituency work."
        expected = ['should', 'attend', 'debates', 'merely', 'strike', 'pairing', 'deals', 'other', 'commitments', 'commons', 'workable', 'suggest', 'three', 'minimum', 'committees', 'leaving', 'least', 'constituency']

        self.assertEqual(get_words(text=text), expected)
    
    # test words count
    def test_generate_records(self):
        words = ['should', 'attend', 'debates', 'merely', 'strike', 'pairing','other', 'deals', 'other', 'commitments', 'commons', 'workable', 'suggest', 'three', 'minimum', 'committees',  'should', 'leaving', 'least', 'constituency', 'should']
        petition_words_counter = Counter(words)

        self.assertEqual(petition_words_counter["should"], 3)
        self.assertEqual(petition_words_counter["other"], 2)
        self.assertEqual(petition_words_counter["attend"], 1)

if __name__ == "__main__":
    unittest.main()