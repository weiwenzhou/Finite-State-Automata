""" Classes and methods for a finite-state automaton (FSA)

A finite-state automaton is defined as a 5-tuple A := (A, Q, I, F, T) such that
A - the English alphabet (a predefined finite, non-empty set)
Q - the set of states
I a proper subset of Q - the set of initial states
F a proper subset of Q - the set of final states
T a proper subset of QxAxQ - the set of transition relations
"""
import numpy as np

class FSA:
    def __init__(self, initial=None, final=set(), transitions={}):
        """ Class for finite-state automata.

        Arugments
        ---------
        initial: obj
            An initial state
            default: None
        final: set
            A set of final states
            default: empty set
        transitions: dict
            dctionary of the form {current_state: {word: {next_state, }, }, }
            default: empty dictionary
        """
        self.INITIAL = initial # obj
        self.FINAL = final # set
        self.TRANSITIONS = transitions # dict
        self.MEM_LETTER = {} # for memoization of letter boolean matrices


        temp_set_of_cur_states = list(transitions.keys()) # list
        # (missing states with no outgoing edges)

        temp_set_of_next_states = {state for edge in transitions.values()
                                            for next in edge.values()
                                            for state in next}
        # (missing states with no incoming edges)

        temp_set_of_next_states.update(temp_set_of_cur_states)
        # Union of the current states and next states

        self.STATES = list(temp_set_of_next_states)

        num = len(self.STATES)
        self.INDICES = {self.STATES[i]:i for i in range(num)} # dict
        self.MATRIX = np.array([["" for col in range(num)] for row in range(num)])

        # fill the matrix with arc_labels
        # row represents the current_state
        # col represents the next_state
        # "" : no edge from row-state to col-state
        for cur, edge in self.TRANSITIONS.items():
            for label, states in edge.items():
                for next in states:
                    self.MATRIX[self.INDICES[cur]][self.INDICES[next]] += label


    def add_final_state(self, state):
        """ Adds state to the set of final states. Returns true if successful, false otherwise."""
        if state in self.STATES:
            self.FINAL.add(state)
            return True
        else:
            return False

    def add_transition(self, current_state, new_state, label):
        """ Adds a transition to the FSA. Returns true if successful, false otherwise."""
        if current_state in self.STATES and new_state in self.STATES:
            # checking if the states are valid

            # add to transitions dictionary
            if self.TRANSITIONS.get(current_state).get(label):
                # check if the current_state already has an edge with the label
                self.TRANSITIONS.get(current_state).get(label).add(new_state)
            else:
                self.TRANSITIONS.get(current_state)[label] = {new_state}

            # add to adjacency matrix
            self.MATRIX[self.INDICES[current_state]][self.INDICES[next]] += label

            return True
        else:
            return False


    def accepts(self, word):
        """Test if FSA accepts the word.

        Arugments
        ---------
        word: string
            A word

        Returns
        -------
        bool
        """

        result = self.get_initial_matrix()
        for letter in word:
            result = result @ self.get_letter_matrix(letter)

        return result @ self.get_final_matrix() != 0

    def get_final_matrix(self):
        """ Returns the boolean matrix representation of the final states. """
        return np.array([1 if state in self.FINAL else 0
                                    for state in self.STATES])

    def get_initial_matrix(self):
        """ Returns the boolean matrix representation of the initial state. """
        return np.array([1 if self.INITIAL == state else 0
                                    for state in self.STATES])

    def get_letter_matrix(self, letter):
        """ Returns the boolean matrix representation of the given letter. """
        if self.MEM_LETTER.get(letter):
            # in the memoization dictionary
            return self.MEM_LETTER.get(letter)
        else:
            # create from scratch
            return np.array([[1 if letter in col else 0 for col in row]
                                    for row in self.MATRIX])

    def remove_final_state(self, state):
        """ Removes state from the set of final states regardless if it is in the
        set or not. """
        self.FINAL.discard(state)

    def set_initial_state(self, state):
        """ Sets the initial state as the new state. Returns true if successful, false otherwise."""
        if state in self.STATES:
            self.INITIAL = state
            return True
        else:
            return False

if __name__ == "__main__":
    fsa = {"I": "X",
           "F": {"Y"},
           "T": { "X": {"a": "Y"},
                  "Y": {"b": "Z"},
                  "Z": {"a": "X"}
                    }
           }
    test = FSA(fsa["I"], fsa["F"], fsa["T"])
    print("Transition matrix")
    print(test.MATRIX)
    print("Inital matrix")
    print(test.get_initial_matrix())
    print("Final matrix")
    print(test.get_final_matrix())
    print("'A' matrix")
    print(test.get_letter_matrix('a'))
    print("aab: " + str(test.accepts('aab')))
    print("aba: " + str(test.accepts('aba')))
    print("a: " + str(test.accepts('a')))
    print("'':" + str(test.accepts('')))

    fsaND = {"I": 0,
           "F": {3},
           "T": {
                    0: {"a": {1, 2} },
                    1: {"c": {1,3}, "b": {2},},
                    2: {"b": {2}, "a": {3}}
                }
           }
    testND = FSA(fsaND["I"], fsaND["F"], fsaND["T"])
    print("Transition matrix")
    print(testND.MATRIX)
    print("Inital matrix")
    print(testND.get_initial_matrix())
    print("Final matrix")
    print(testND.get_final_matrix())
    print("'A' matrix")
    print(testND.get_letter_matrix('a'))
    print("aa: " + str(testND.accepts('aa')))
    print("acbba: " + str(testND.accepts('acbba')))
    print("abba: " + str(testND.accepts('abba')))
    print("abab: " + str(testND.accepts('abab')))
    print("'':" + str(testND.accepts('')))

    # I = testND.get_initial_matrix()
    # A = testND.get_letter_matrix('a')
    # B = testND.get_letter_matrix('b')
    # F = testND.get_final_matrix()

    # print(A)
    # print(B)
    # result = I
    # result = result @ A
    # result = result @ B
    # result = result @ B
    # result = result @ A
    # result = result @ F
    # print(result)
