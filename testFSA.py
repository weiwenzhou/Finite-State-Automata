from FSA import *

import random
import string
from hypothesis import given, settings
import hypothesis.strategies as st


def empty():
    """ Returns an empty fsa. """
    return FSA(set(), set(), [])

def random_fsa():
    """ Returns a random valid fsa. """
    states = set()
    for x in range(random.randint(0, 20)):
        states.add(st.text(alphabet=string.ascii_letters, min_size=1))
    length = len(states)
    # pick initial
    I = set(random.sample(states, random.randint(0, length)))
    # pick final
    F = set(random.sample(states, random.randint(0, length)))

    # pick transition
    T = []
    for x in range(random.randint(0, length)):
        cur = random.sample(states, 1)[0]
        l = str(st.text(alphabet=string.ascii_letters, min_size=1))
        next = random.sample(states, 1)[0]
        T.append((cur, l, next))

    return FSA(I, F, T)

# add
@given(states=st.sets(st.text(alphabet=string.ascii_letters, min_size=1), min_size = 1, max_size = 10))
@settings(max_examples=100)
def test_add_state(states):
    """ Add a random number of states. """
    tester = random_fsa()
    orig = tester.STATES.copy()

    for state in states:
        tester.add_state(state)
        orig.add(state)

    assert tester.STATES == orig

@given(state = st.text(alphabet=string.ascii_letters, min_size=1))
@settings(max_examples=100)
def test_add_initial_state(state):
    """ start with an empty fsa with defined states.

    An initial state can be
    1. valid in the set of states
    2. invalid not in the set of states
    """
    tester = random_fsa()
    orig = tester.INITIAL.copy()
    tester.add_initial_state(state)
    if state in tester.STATES:
        orig.add(state)
    assert tester.INITIAL == orig

@given(state = st.text(alphabet=string.ascii_letters, min_size=1))
@settings(max_examples=100)
def test_add_final_state(state):
    """ similar to add initial state """
    tester = random_fsa()
    orig = tester.FINAL.copy()
    tester.add_final_state(state)
    if state in tester.STATES:
        orig.add(state)
    assert tester.FINAL == orig

@given(states=st.sets(st.text(alphabet=string.ascii_letters, min_size=1), min_size = 1, max_size = 10),
            transition = st.tuples(st.text(alphabet=string.ascii_letters, min_size=1),
                                   st.text(alphabet=string.ascii_letters, min_size=1),
                                   st.text(alphabet=string.ascii_letters, min_size=1)))
@settings(max_examples=100)
def test_add_transition(states, transition):
    tester = empty()
    tester.STATES = states


# get
def test_get_initial_matrix():
    pass

def test_get_final_matrix():
    pass

def test_get_letter_matrix():
    pass

# remove
def test_remove_state():
    pass

def test_remove_initial_state():
    pass

def test_remove_final_state():
    pass

def test_remove_transition():
    pass

# accepts
def test_accepts():
    pass


if __name__ == "__main__":
    from pprint import pprint

    fsa = {"I": {"X"},
           "F": {"Y"},
           "T": [
                ("X", "a", "Y"),
                ("Y", "b", "Z"),
                ("Z", "a", "X")
                ]
           }

    print(fsa)
    test = FSA(fsa["I"], fsa["F"], fsa["T"])
    print("Transitions")
    pprint(test.TRANSITIONS, width=1)
    print("STATES")
    print(test.STATES)
    print("Inital matrix")
    print(test.get_initial_matrix())
    print("Final matrix")
    print(test.get_final_matrix())
    print("'a' matrix")
    print(test.get_letter_matrix('a'))
    print("aab: " + str(test.accepts('aab'))) # False
    print("aba: " + str(test.accepts('aba'))) # False
    print("a: " + str(test.accepts('a'))) # True
    print("abaa: " + str(test.accepts('abaa'))) # True
    print("'':" + str(test.accepts(''))) # False

    """
    pprint(test.MEM_LETTER)
    test.add_state("W");
    print(f"States: {test.STATES}")
    print()
    print("Inital matrix")
    print(test.get_initial_matrix())
    print("Final matrix")
    print(test.get_final_matrix())
    print("a: " + str(test.accepts('a'))) # True
    pprint(test.MEM_LETTER)
    """

    print("REMOVE TESTING")
    print("REMOVE STATE")
    print(test.STATES)
    print(test.TRANSITIONS)
    print(test.INITIAL)
    print(test.FINAL)

    # test.remove_state("X")
    # test.remove_state("Y")
    # test.remove_state("W") # boundary test

    # test.remove_transition("X","a", "Z")
    # test.remove_transition("Z", "a", "X")
    # test.remove_transition("W", "1", "V") # boundary test

    print("AFTER")
    print(test.STATES)
    print(test.TRANSITIONS)
    print(test.INITIAL)
    print(test.FINAL)
