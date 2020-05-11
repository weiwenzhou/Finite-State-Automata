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
        states.add("".join(random.choice(string.ascii_letters)))
    length = len(states)
    # pick initial
    I = set(random.sample(states, random.randint(0, length)))
    # pick final
    F = set(random.sample(states, random.randint(0, length)))

    # pick transition
    T = []
    for x in range(random.randint(0, length)):
        cur = random.sample(states, 1)[0]
        l = "".join(random.choice(string.ascii_letters))
        next = random.sample(states, 1)[0]
        T.append((cur, l, next))

    return FSA(I, F, T)

# add
@given(states=st.sets(st.text(alphabet=string.ascii_letters, min_size=1, max_size=1), min_size = 1, max_size = 10))
@settings(max_examples=100)
def test_add_state(states):
    """ Add a random number of states. """
    tester = random_fsa()
    orig = tester.STATES.copy()

    for state in states:
        tester.add_state(state)
        orig.add(state)

    assert tester.STATES == orig

@given(state = st.text(alphabet=string.ascii_letters, min_size=1, max_size=1))
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

@given(state = st.text(alphabet=string.ascii_letters, min_size=1, max_size=1))
@settings(max_examples=100)
def test_add_final_state(state):
    """ similar to add initial state """
    tester = random_fsa()
    orig = tester.FINAL.copy()
    tester.add_final_state(state)
    if state in tester.STATES:
        orig.add(state)
    assert tester.FINAL == orig

@given(transition = st.tuples(st.text(alphabet=string.ascii_letters, min_size=1, max_size=1),
                              st.text(alphabet=string.ascii_letters+string.digits),
                              st.text(alphabet=string.ascii_letters, min_size=1, max_size=1)))
@settings(max_examples=100)
def test_add_transition(transition):
    tester = random_fsa()
    orig = tester.TRANSITIONS.copy()

    cur, l, next = transition
    tester.add_transition(cur, l, next)

    # l is a string already as defined
    if l.isalpha() and len(l) == 1:
        orig[cur] = orig.get(cur, {})
        temp = orig[cur].get(next, set())
        temp.add(l)
        orig[cur][next] = temp

    assert tester.TRANSITIONS == orig


# get
"""
@settings(max_examples=100)
def test_get_initial_matrix():
    pass

@settings(max_examples=100)
def test_get_final_matrix():
    pass

@settings(max_examples=100)
def test_get_letter_matrix():
    pass
"""

# remove
@given(state = st.text(alphabet=string.ascii_letters, min_size=1, max_size=1))
@settings(max_examples=100)
def test_remove_state(state):
    tester = random_fsa()
    S = tester.STATES.copy()
    T = tester.TRANSITIONS.copy()

    tester.remove_state(state)

    # not testing the remove methods here so we can assume they work as intended
    tester.remove_initial_state(state)
    tester.remove_final_state(state)
    I = tester.INITIAL.copy()
    F = tester.FINAL.copy()

    if state in S:
        S.remove(state)

    if state in T:
        del T[state]

    for edges in T.values():
        if state in edges:
            del edges[state]

    assert tester.STATES == S and tester.TRANSITIONS == T

@given(state = st.text(alphabet=string.ascii_letters, min_size=1, max_size=1))
@settings(max_examples=100)
def test_remove_initial_state(state):
    tester = random_fsa()
    orig = tester.INITIAL.copy()
    tester.remove_initial_state(state)
    if state in orig:
        orig.remove(state)
    assert tester.INITIAL == orig

@given(state = st.text(alphabet=string.ascii_letters, min_size=1, max_size=1))
@settings(max_examples=100)
def test_remove_final_state(state):
    tester = random_fsa()
    orig = tester.FINAL.copy()
    tester.remove_final_state(state)
    if state in orig:
        orig.remove(state)
    assert tester.FINAL == orig

@given(transition = st.tuples(st.text(alphabet=string.ascii_letters, min_size=1, max_size=1),
                              st.text(alphabet=string.ascii_letters+string.digits),
                              st.text(alphabet=string.ascii_letters, min_size=1, max_size=1)))
@settings(max_examples=100)
def test_remove_transition(transition):
    tester = random_fsa()
    orig = tester.TRANSITIONS.copy()

    cur, l, next = transition
    tester.remove_transition(cur, l, next)

    # l is a string already as defined
    if l.isalpha() and len(l) == 1 and cur in orig and next in orig[cur] and l in orig[cur][next]:
        # l is alphabet and length 1
        # cur has an outgoing edge
        # there is an edge from cur to next
        # l is a label of that edge

        # delete that transition
        orig[cur][next].remove(l)

    assert tester.TRANSITIONS == orig

# accepts
@given(word = st.text(alphabet=string.ascii_letters))
@settings(max_examples=100)
def test_accepts(word):
    # copy paste because parsing is easier with transition tuple
    states = set()
    for x in range(random.randint(0, 20)):
        states.add("".join(random.choice(string.ascii_letters)))
    length = len(states)
    # pick initial
    I = set(random.sample(states, random.randint(0, length)))
    # pick final
    F = set(random.sample(states, random.randint(0, length)))

    # pick transition
    T = []
    # dictionary for parsing
    trans = {}
    for x in range(random.randint(0, length)):
        cur = random.sample(states, 1)[0]
        l = "".join(random.choice(string.ascii_letters))
        next = random.sample(states, 1)[0]
        T.append((cur, l, next))

        trans[cur] = trans.get(cur, {})
        temp = trans[cur].get(l, set())
        temp.add(next)
        trans[cur][l] = temp

    tester = FSA(I, F, T)

    if word == "":
        # empty string condition
        # true if initial and final contains a state that is the same
        truth = True if tester.INITIAL.intersection(tester.FINAL) else False
    else:
        def check_initial():
            """ Returns true if there is a valid path through the
            transition dictionary for the word. """
            def parse(start, word):
                if word == "":
                    return True
                else:
                    next = trans.get(cur, {}).get(word[0], {})
                    while next:
                        if parse(next.pop(), word[1:]):
                            return True
                    return False

            I = tester.INITIAL.copy()
            while I:
                if parse(I.pop(), word):
                    return True
            return False
        truth = check_initial()

    assert tester.accepts(word) == truth

if __name__ == "__main__":
    from pprint import pprint

    """TESTING BOOLEAN MATRICES methods """

    fsa = {"I": {"X"},
           "F": {"Y"},
           "T": [
                ("X", "a", "Y"),
                ("Y", "b", "Z"),
                ("Z", "a", "X")
                ]
           }

    test = FSA(fsa["I"], fsa["F"], fsa["T"])

    print("CHECKING GETTERS")
    print("STATES")
    print(test.STATES)

    print(f"Initials {test.INITIAL}")
    print("Inital matrix")
    print(test.get_initial_matrix())

    print("Final matrix")
    print(f"Initials {test.FINAL}")
    print(test.get_final_matrix())

    print("'a' matrix")
    print("Transitions")
    pprint(test.TRANSITIONS, width=1)
    print(test.get_letter_matrix('a'))


    print("\nTESTING ACCEPTS")
    print("aab: " + str(test.accepts('aab'))) # False
    print("aba: " + str(test.accepts('aba'))) # False
    print("a: " + str(test.accepts('a'))) # True
    print("abaa: " + str(test.accepts('abaa'))) # True
    print("'':" + str(test.accepts(''))) # False

    print("\nTESTING memoization")
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
    print("\nREMOVE TESTING")
    print("REMOVE STATE")
    print(test.STATES)
    print(test.TRANSITIONS)
    print(test.INITIAL)
    print(test.FINAL)

    # Uncomment to test

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

    # test.add_transition("X", 0, "X")
    """
