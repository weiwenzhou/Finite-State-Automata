from FSA import *
import os # for clearing the terminal
from pprint import pprint

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

#
# THESE ARE JUST MESSAGES TO THE USER
#

menu_message = """
What do you to do:
Add     [A/add]
Matrix  [M/matrix]
Remove  [R/remove]
View    [V/view]
[C/clear] to clear the screen
[Q/quit] to quit
$ """

add_message = """
What do you want to add:
1. Final state [F/final]
2. Inital state[I/initial]
3. A new state [S/state]
4. A transition[T/transition]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ """

remove_message = """
What do you want to remove:
1. Final state [F/final]
2. Inital state[I/initial]
3. A new state [S/state]
4. A transition[T/transition]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ """

matrix_message = """
What do you want to view:
1. Final matrix [F/final]
2. Inital matrix[I/initial]
3. Letter matrix[L/letter]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ """

view_message = """
What do you want to view:
1. Final states [F/final]
2. Inital states[I/initial]
3. states       [S/state]
4. Transitions  [T/transition]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ """
# interactive interface for other methods
print("This is interacting with my_fsa by default")
# you can change which one you are interacting with by adjusting the
# variable below
interactive = my_fsa

running = True
while running:
    user = input(menu_message).lower()

    # ADD
    if user == 'a' or user == 'add':
        adding = True
        while adding:
            user_add = input(add_message).lower()

            if user_add == 'f' or user_add == 'final':
                state = input("Enter the final state: ")
                interactive.add_final_state(state)

            if user_add == 'i' or user_add == 'inital':
                state = input("Enter the initial state: ")
                interactive.add_initial_state(state)

            if user_add == 's' or user_add == 'state':
                state = input("Enter the state: ")
                interactive.add_state(state)

            if user_add == 't' or user_add == 'transition':
                cur = input("Enter the starting state of the transition: ")
                next = input("Enter the next state of the transition: ")
                label = input("Enter the arc label of the transition: ")
                interactive.add_transition(cur, label, next)

            if user_add == 'b' or user_add == 'back':
                adding = False

            if user_add == 'c' or user_add == 'clear':
                os.system('clear')

            if user_add == 'q' or user_add == 'quit':
                adding = False
                running = False

    # MATRIX
    if user == 'm' or user == 'matrix':
        matrix_view = True
        while matrix_view:
            user_add = input(matrix_message).lower()

            if user_add == 'f' or user_add == 'final':
                print(interactive.get_final_matrix())

            if user_add == 'i' or user_add == 'inital':
                print(interactive.get_initial_matrix())

            if user_add == 'l' or user_add == 'letter':
                letter = input("Enter the letter: ")
                pprint(interactive.get_letter_matrix(letter))

            if user_add == 'b' or user_add == 'back':
                matrix_view = False

            if user_add == 'c' or user_add == 'clear':
                os.system('clear')

            if user_add == 'q' or user_add == 'quit':
                matrix_view = False
                running = False


    # REMOVE
    if user == 'r' or user == 'remove':
        removing = True
        while removing:
            user_add = input(remove_message).lower()

            if user_add == 'f' or user_add == 'final':
                state = input("Enter the final state: ")
                interactive.remove_final_state(state)

            if user_add == 'i' or user_add == 'inital':
                state = input("Enter the initial state: ")
                interactive.remove_initial_state(state)

            if user_add == 's' or user_add == 'state':
                state = input("Enter the state: ")
                interactive.remove_state(state)

            if user_add == 't' or user_add == 'transition':
                cur = input("Enter the starting state of the transition: ")
                next = input("Enter the next state of the transition: ")
                label = input("Enter the arc label of the transition: ")
                interactive.remove_transition(cur, label, next)

            if user_add == 'b' or user_add == 'back':
                removing = False

            if user_add == 'c' or user_add == 'clear':
                os.system('clear')

            if user_add == 'q' or user_add == 'quit':
                removing = False
                running = False

    if user == 'v' or user == 'view':
        viewing = True
        while viewing:
            user_add = input(view_message).lower()

            if user_add == 'f' or user_add == 'final':
                print(interactive.FINAL)

            if user_add == 'i' or user_add == 'inital':
                print(interactive.INITIAL)


            if user_add == 's' or user_add == 'state':
                print(interactive.STATES)

            if user_add == 't' or user_add == 'transition':
                pprint(interactive.TRANSITIONS, width=1)

            if user_add == 'b' or user_add == 'back':
                viewing = False

            if user_add == 'c' or user_add == 'clear':
                os.system('clear')

            if user_add == 'q' or user_add == 'quit':
                viewing = False
                running = False

    if user == 'q' or user == 'quit':
        # ends the loop
        running = False

    if user == 'c' or user == 'clear':
        # clears the terminal
        os.system('clear')
