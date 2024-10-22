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
    def __init__(self, initial=set(), final=set(), transitions=[]):
        """ Class for finite-state automata.

        Arugments
        ---------
        initial: set
            An initial state
            default: None
        final: set
            A set of final states
            default: empty set
        transitions: list
            list of tuples of the form (current_state, label, next_state)
            default: []
        """
        self.INITIAL = set()
        self.FINAL = set()
        self.STATES = set() # set
        self.TRANSITIONS = dict() # dict
        for transition in transitions:
            self.add_transition(*transition);
        self.MEM_LETTER = {} # for memoization of letter boolean matrices

        # need to check if the given initial and final are valid
        for state in initial:
            self.add_initial_state(state)
        for state in final:
            self.add_final_state(state)

    def add_initial_state(self, state):
        """ Adds state to the set of initial states.
        Returns true if successful, false otherwise."""
        if state in self.STATES:
            self.INITIAL.add(state)
            return True
        else:
            print(f"The state {state} has not been added to inital because it is not in the set of states.")
            return False

    def add_final_state(self, state):
        """ Adds state to the set of final states.
        Returns true if successful, false otherwise."""
        if state in self.STATES:
            self.FINAL.add(state)
            return True
        else:
            print(f"The state {state} has not been added to final because it is not in the set of states.")
            return False

    def add_state(self, state):
        """ Adds a state into the set of states of the FSA. """
        if state not in self.STATES:
            self.STATES.add(state)
            self.MEM_LETTER.clear()
            # the old memoize matrices no longer work with the numbers of states now

    def add_transition(self, current_state, label, new_state):
        """ Adds a transition to the FSA.
        Returns true if successful, false otherwise.

        TRANSITIONS = {
            s0: {
                    s0: {arc_labels0, arc_labels1},
                    s1: {...},
                    ...,
                    sn
                },
            s1: {...},
            ...,
            sn
        }
        """
        # check if the label is in the set of alphabet
        if isinstance(label, str) and label.isalpha() and len(label) == 1:
            # the label is in the set of alphabet
            # add current_state and new_state to set of states
            self.STATES.add(current_state)
            self.STATES.add(new_state)

            # add the transition to the transition dictionary
            self.TRANSITIONS[current_state] = self.TRANSITIONS.get(current_state, {})
            if self.TRANSITIONS[current_state].get(new_state):
                # there is already an edge between the two states
                self.TRANSITIONS[current_state][new_state].add(label)
            else:
                # no edges yet
                self.TRANSITIONS[current_state][new_state] = {label}

            return True
        else:
            # the label is not in the set of alphabet
            print(f"The transition tuple ({current_state}, {label}, {new_state}) is not added because the label {label} is not in the set of alphabet")
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
        return np.array([1 if state in self.INITIAL else 0
                                    for state in self.STATES])

    def get_letter_matrix(self, letter):
        """ Returns the boolean matrix representation of the given letter. """
        if letter in self.MEM_LETTER:
            # in the memoization dictionary
            return self.MEM_LETTER.get(letter)
        else:
            # create from scratch
            matrix = np.array([[1 if (letter in self.TRANSITIONS.get(cur,{}).get(next, {}))
                                else 0 for next in self.STATES]
                                        for cur in self.STATES])
            # memoize
            self.MEM_LETTER[letter] = matrix
            return matrix

    def remove_initial_state(self, state):
        """ Removes state from the set of final states regardless if it is in the
        set or not. """
        self.INITIAL.discard(state)

    def remove_final_state(self, state):
        """ Removes state from the set of final states regardless if it is in the
        set or not. """
        self.FINAL.discard(state)

    def remove_state(self, state):
        """ Removes a state from the fsa. This includes removing the given state
        from the set of initial states, the set of final states, and the set of
        transition relations. """
        if state in self.STATES:
            # remove from states
            self.STATES.discard(state)
            # remove from initial
            self.remove_initial_state(state)
            # remove from final
            self.remove_initial_state(state)

            # remove from transitions
            # outgoing edges
            if state in self.TRANSITIONS:
                # if there are transitions going out
                self.TRANSITIONS.pop(state)
            # incoming edges
            for edges in self.TRANSITIONS.values():
                if state in edges:
                    edges.pop(state)

    def remove_transition(self, current_state, label, new_state):
        """ Removes a transition from the set of transition relations. """
        # check if transition exists
        if label in self.TRANSITIONS.get(current_state, {}).get(new_state, {}):
            self.TRANSITIONS[current_state][new_state].discard(label)
