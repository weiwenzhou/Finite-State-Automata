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
        pass

    def add_final_state(self, state):
        """ Adds state to the set of final states. """
        pass

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

    def get_final_state(self):
        """ Returns the set of final states. """
        pass

    def get_initial_state(self):
        """ Returns the intial state. """
        pass

    def remove_final_state(self, state):
        """ Removes state from the set of final states regardless if it is in the
        set or not. """
        pass

    def set_initial_state(self, state):
        """ Sets the initial state as the new state. """
        pass
