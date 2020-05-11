from FSA import *

import random
import string
from hypothesis import given, settings
import hypothesis.strategies as st


def empty():
    """ Returns an empty fsa. """
    return FSA(set(), set(), [])

# add
@given(states=st.sets(st.text(alphabet=string.ascii_letters, min_size=1), min_size = 1, max_size = 10))
@settings(max_examples=100)
def test_add_state(states):
    """ start with an empty fsa and add a random number of states. """
    tester = empty()
    for state in states:
        tester.add_state(state)

    assert tester.STATES == states

@given(states=st.sets(st.text(alphabet=string.ascii_letters, min_size=1), min_size = 1, max_size = 10),
            extra = st.text(alphabet=string.ascii_letters, min_size=1))
@settings(max_examples=100)
def test_add_initial_state(states, extra):
    """ start with an empty fsa with defined states.

    An initial state can be
    1. valid in the set of states
    2. invalid not in the set of states
    """
    tester = empty()
    tester.STATES = states

    tester.add_initial_state(extra)

    if extra in states:
        assert tester.INITIAL == {extra}
    else:
        assert tester.INITIAL == set()



@given(states=st.sets(st.text(alphabet=string.ascii_letters, min_size=1), min_size = 1, max_size = 10),
            extra = st.text(alphabet=string.ascii_letters, min_size=1))
@settings(max_examples=100)
def test_add_final_state(states, extra):
    """ similar to add initial state """
    tester = empty()
    tester.STATES = states

    tester.add_final_state(extra)

    if extra in states:
        assert tester.FINAL == {extra}
    else:
        assert tester.FINAL == set()

def test_add_transition():
    pass

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
