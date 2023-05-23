import unittest

from knight_moves_sequences import get_key_sequences


class KeySequencesTestCase(unittest.TestCase):
    def test_get_key_sequences(self):
        knight_hop = {
            "A": [["H", "L"], True],
            "B": [["K", "M", "I"], False],
            "C": [["F", "J", "L", "N"], False],
            "D": [["G", "M", "O"], False],
            "E": [["H", "N"], True],
            "F": [["C", "M"], False],
            "G": [["D", "N", "2"], False],
            "H": [["A", "E", "K", "O", "1", "3"], False],
            "I": [["B", "L", "2"], True],
            "J": [["C", "M"], False],
            "K": [["B", "H", "2"], False],
            "L": [["A", "C", "I", "3"], False],
            "M": [["B", "D", "F", "J"], False],
            "N": [["C", "E", "G", "1"], False],
            "O": [["D", "H", "2"], True],
            "1": [["F", "H", "N"], False],
            "2": [["G", "I"], False],
            "3": [["H", "J", "L"], False]
        }

        totalKeysInSequence = 10

        # Test the total number of valid key sequences
        valid_sequences = get_key_sequences(knight_hop)
        self.assertEqual(valid_sequences, 1209580)


if __name__ == '__main__':
    unittest.main()
