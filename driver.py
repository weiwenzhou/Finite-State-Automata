from FSA import *


def read_file(path):
    """ Returns the fsa defined by the input file """
    f = open(path)
    lines = f.readlines()
    f.close()
    # first 2 lines are initial and final states
    I = lines[0].strip().split(" ")
    F = lines[1].strip().split(" ")
    # the rest are transition relations
    T = []
    for line in lines[2:]:
        # only the first 3 are looked at
        cur, l, next = tuple(line.strip().split(" ")[:3])
        T.append((cur, l, next))

    return FSA(I, F, T)
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
my_fsa1 = read_file("INPUT/example.txt")

words_to_test = ["aab", "aba", "a", "abaa", ""]
# should be [False, False, True, True, False]

print("my_fsa")
for word in words_to_test:
    print(f"'{word}': {my_fsa.accepts(word)}")

print("my_fsa1 read from example.txt")
for word in words_to_test:
    print(f"'{word}': {my_fsa1.accepts(word)}")

# You can also try the under methods to manipulate your fsa without having to
# change the variables are the start
