from FSA import *

# To define your FSA

# You can play around with these variables.
# Note I and F should be a set
# and T is an array of tuples of the form (current_state, label, next_state)
I = {"X"} # Initial
F = {"Y"} # Final
T = [   ("X", "a", "Y"),
        ("Y", "b", "Z"),
        ("Z", "a", "X")] # Transition relations

my_fsa = FSA(I, F, T)

words_to_test = ["aab", "aba", "a", "abaa", ""]
# should be [False, False, True, True, False]

for word in words_to_test:
    print(f"'{word}': {my_fsa.accepts(word)}")

# You can also try the under methods to manipulate your fsa without having to
# change the variables are the start
