# Key Sequences

This project calculates the total number of valid key sequences given a set of key movements. It uses a backtracking algorithm to explore all possible key sequences and determines the count of valid sequences.

## Key Movements

The key movements are defined in the `knight_hop` dictionary. Each key is associated with a list of possible next keys and a boolean value indicating whether it is a vowel. For example:

knight_hop = {
"A": [["H", "L"], True],
"B": [["K", "M", "I"], False],
...
}


## Usage

To calculate the total number of valid key sequences:

1. Modify the `totalKeysInSequence` variable in the code to set the desired sequence length.
2. Run the script by executing the following command:

python key_sequences.py


The output will display the total number of valid key sequences of the specified length.

## Optimization

Efforts have been made to optimize the code for performance and readability. The backtracking algorithm is used to efficiently explore the key sequences and count the valid ones. However, please ensure that the problem size is within reasonable limits to avoid excessive computation time and memory usage.

## License

This project is licensed under the [MIT License](LICENSE).


