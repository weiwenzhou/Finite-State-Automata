from matrix import *

class FSA:
    def __init__(self, initial=None, final=set(), transitions={}):
        """ Class for deterministic finite-state automata.

        Arugments
        ---------
        initial: obj
            An initial state
            default: None
        final: set
            A set of final states
            default: empty set
        transitions: dict
            dctionary of the form {arc_label: {current_state: next_state, }, }
            default: empty dictionary
        """
        self.INITIAL = initial # obj
        self.FINAL = final # set
        self.TRANSITIONS = transitions # dict
        self.STATES = transitions.keys() # list

        num = len(self.STATES.length)
        self.MATRIX = np.array([["" for col in range(num)] for row in range(num)])

        # fill the matrix with arc_labels
        # row represents the current_state
        # col represents the next_state
        # "" : no edge from row-state to col-state
        for label, edge in self.TRANSITIONS.items():
            for cur, next in edge.items():
                self.MATRIX[cur][next] += label

    def add_final_state(self, state):
        """ Adds state to the set of final states.

        Raises
        ------
        ValueError
            When the given state is not in the list of states
        """
        if state in self.STATES:
            self.FINAL.add(state)
        else:
            raise ValueError("Invalid state cannot be assigned as a final state")

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
        pass

    def get_final_matrix(self):
        """ Returns the boolean matrix representation of the final states. """
        pass

    def get_final_state(self):
        """ Returns the set of final states. """
        return self.FINAL

    def get_initial_matrix(self):
        """ Returns the boolean matrix representation of the initial state. """
        pass

    def get_initial_state(self):
        """ Returns the intial state. """
        return self.INITIAL

    def get_letter_matrix(self, letter):
        """ Returns the boolean matrix representation of the given letter. """
        pass

    def get_states(self):
        """ Returns the list of states. """
        return self.STATES

    def get_transitions(self):
        """ Returns the dictionary of transitions. """
        return self.TRANSITIONS

    def get_transitions_matrix(self):
        """ Returns a 2-D matrix representation of transitions """
        pass

    def remove_final_state(self, state):
        """ Removes state from the set of final states regardless if it is in the
        set or not. """
        self.FINAL.discard(state)

    def set_initial_state(self, state):
        """ Sets the initial state as the new state.

        Raises
        ------
        ValueError
            When the given state is not in the list of states
        """
        if state in self.STATES:
            self.INITIAL = state
        else:
            raise ValueError("Invalid state cannot be assigned as the inital state")
