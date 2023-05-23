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

count_seq = 0
vowels_to_use = 2
totalKeysInSequence = 10

def get_key_sequences(key_dict):
    """
    Get the total number of valid key sequences of length `totalKeysInSequence`.

    Args:
        key_dict (dict): Dictionary representing the key movements compling with knight moves.

    Returns:
        int: Total number of valid key sequences.

    """
    global vowels_to_use

    for key in key_dict:
        seq = get_candidates(key, vowels_to_use, totalKeysInSequence)

    return seq


def get_candidates(key, vowels, unused):
    """
    Recursively explore the possible key sequences.

    Args:
        key (str): Current key.
        vowels (int): Number of vowels remaining to be used.
        unused (int): Number of unused keys remaining in the sequence.

    Returns:
        int: Number of valid key sequences.

    """
    global count_seq

    unused -= 1
    vowels -= int(knight_hop[key][1])

    for i in knight_hop[key][0]:
        if unused > 0:
            if vowels > 0 or not knight_hop[key][1]:
                get_candidates(i, vowels, unused)
        else:
            count_seq += 1

    return count_seq


if __name__ == '__main__':
    """Main function"""

    print("Total number of valid {} key sequences are: {}".format(
        totalKeysInSequence, get_key_sequences(knight_hop)))
