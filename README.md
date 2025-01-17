# LIN 220 Project for Spring 2020

Finite-state automata as Boolean matrix multiplication (Difficulty: 3, but can be done by a single person)

This project is for the mathematically inclined only. Finite-state automata can be represented as a collection of matrices where all cells are either True or False. These are called Boolean matrices. The process of determining whether a string is accepted by an automaton is equivalent to a specific sequence of matrix multiplications.

This project involves two components:
1. Read up on the connection between automata and Boolean matrix multiplication. The reading materials will be supplied by me, but you should be comfortable reading mathematical notation. [Link for FSA](https://github.com/stonybrook-lin539-f19/main/blob/master/pdf/05_automata/01_automata.pdf), [Link for FSA w/ BMM](https://github.com/stonybrook-lin539-f19/main/blob/master/pdf/05_automata/06_matrix_representation.pdf)
2. Implement code that converts an automaton into its equivalent Boolean matrix representation, as well as an alternative to the .accepts method that uses Boolean matrix multiplication. As part of this, you will have to learn how matrices are handled in Python.

Used techniques: memoization for matrix multiplication, the numpy package for representing matrices and matrix multiplication

## Getting Started
Clone this repo with either ssh or http
```
$ git clone git@github.com:wzhou2/LIN220-Project.git
or
$ git clone https://github.com/wzhou2/LIN220-Project.git
```

### Dependencies
Python external libraries required to run this program:
* Numpy:       For matrix multiplication
* Pytest:      For testing
* Hypothesis:  For testing

To install the dependencies run this in the project directory:
```
../LIN220-Project$ pip install -r requirements.txt
```

## Project Details and Approach
In this project, we replicated finite-state automaton as defined:

A finite-state automaton is defined as a 5-tuple A := (A, Q, I, F, T) such that

1. A - the English alphabet (a predefined finite, non-empty set)
2. Q - the set of states
3. I a proper subset of Q - the set of initial states
4. F a proper subset of Q - the set of final states
5. T a proper subset of QxAxQ - the set of transition relations

A string, s, is recognized by A if and if there is a some run of A over s, in which the last component of the run is a final state. 

We will do a run of A over s with boolean matrix multiplication.
In order to do this:
Given N is the number of elements in Q (the set of states).
We will have matrices for the initial states, final states, and for each letter in the string s:

* The matrix for the initial states is a 1 by N matrix with each column of the matrix representating  a state in the FSA. The value of an entry in the matrix is 1 if the state representating the column of the matrix is an initial state, otherwise it will be 0. 

* The matrix for the final states is a N by 1 matrix with each row of the matrix representating a state in the FSA. The value of an entry in the matrix is a 1 if the state representating the row of the matrix is a final state, otherwise it will be 0.

* For each letter in the string s, we will create a N by N matrix, with the rows representation current state and the columns representation the next state, filled with 1s and 0s. A position is a 1 if there is an edge going from row state to a column state, otherwise it will be 0.

To do the run:
Given a string s defined as "c0c1c2...cn" where c represents a letter in the string, we will multiply the matrices in this order.

Note: M(I), M(F), and M(c) are the matrix representation as defined for the initial states, final states, and each letter in the string.

M(I) times M(c0) times M(c1) time M(c2) times ... times M(cn) times M(F) = result.

A string is accepted if and only if the result is nonzero. 

## Implementation
To implement finite-state automata recognization with boolean matrix multiplication in Python, we will be using python classes, python sets for maintaining lists with no duplicates, python dictionaries, and numpy for matrix multiplication.

We will be creating a class called FSA that serves as the finite-state automata.
The class will contain the attributes:

```
INITIAL:     The set of initial states
FINAL:       The set of final states
STATES:      The set of states
TRANSITIONS: The dictionary containing the edges for the FSA
    This is the format for how the dictionary should look like with s0,s1,...,sn 
    representing the states and arc_label is a single letter alphabetic character 
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
MEM_LETTER:  The dictionary containing the boolean letter matrices that have 
                already been used for memoization
```

For the constructor of the class:
```
FSA(initial, final, transition)
Initial:     A collection of the initial states. (list, tuple, set, etc)
Final:       A collection of the final states. (list, tuple, set, etc)
Transitions: A collection of tuples of the form 
                (current_state, label, next_state) representating the transition relations

fsa = FSA(  {"X"}, 
            {"Y"},
            [   ("X", "a", "Y"),
                ("Y", "b", "Z"),
                ("Z", "a", "X")] )
```

### Methods

##### FSA.accepts(self, word)
Tests if there is valid run of the FSA over the word.
```
fsa.accepts('aab') # returns False
fsa.accepts('aba') # returns False
fsa.accepts('a') # returns True
fsa.accepts('abaa') # returns True
fsa.accepts('') # returns False
```

##### FSA.add_state(self, state)
Adds the state to the FSA.
```
fsa.STATES returns {"X", "Y", "Z"}
fsa.add_state("W")
fsa.STATES returns {"X", "Y", "Z", "W"}
```

##### FSA.add_initial_state(self, state)
Adds the state as an initial state of the FSA.
```
fsa.INITIAL returns {"X"}
fsa.add_initial_state("Y") returns True
fsa.INITIAL returns {"X", "Y")
fsa.add_initial_states("J") returns False
    Also prints -> The state J has not been added because it is not in the set of states.
```

##### FSA.add_final_state(self, state)
Adds the state as an initial state of the FSA.
```
fsa.FINAL returns {"Y"}
fsa.add_final_state("X") returns True
fsa.FINAL returns {"Y", "X")
fsa.add_final_states("J") returns False
    Also prints: The state J has not been added because it is not in the set of states.
```

##### FSA.add_transition(self, current_state, label, new_state)
Adds the transition from the current_state to the new_state with the label as its label.
```
fsa.TRANSITIONS 
    returns {   'X': {'Y': {'a'}},
                'Y': {'Z': {'b'}},
                'Z': {'X': {'a'}} }
fsa.add_transition("X", "c", "X") returns True
fsa.TRANSITIONS 
    returns {   'X': {'X': {'c'}, 'Y': {'a'}},
                'Y': {'Z': {'b'}},
                'Z': {'X': {'a'}} }
fsa.add_transition("X", "cc", "X") returns False
    Also prints: The transition tuple (X, cc, X) is not added 
                    because the label cc is not in the set of alphabet
fsa.add_transition("X", "0", "X"} returns False
    Also prints: The transition tuple (X, 0, X) is not added 
                    because the label 0 is not in the set of alphabet
```

##### FSA.get_initial_matrix(self)*
Returns the boolean initial matrix. 
```
fsa.INITIAL returns {"X"}
fsa.STATES returns {"X", "Y", "Z"}

fsa.get_inital_matrix() returns [1, 0, 0]
```
##### FSA.get_final_matrix(self)*
Returns the boolean final matrix.
```
fsa.FINAL returns {"Y"}
fsa.STATES returns {"X", "Y", "Z"}

fsa.get_final_matrix() returns [0, 1, 0]
```

##### FSA.get_letter_matrix(self, letter)*
Returns the boolean matrix for the given letter.
```
fsa.TRANSITIONS 
    returns {   'X': {'Y': {'a'}},
                'Y': {'Z': {'b'}},
                'Z': {'X': {'a'}} }
fsa.STATES returns {"X", "Y", "Z"}
fsa.get_letter_matrix("a") 
    returns [ [0, 1, 0], # X
              [0, 0, 0], # Y
              [1, 0, 0]] # Z
             # X  Y  Z
```

###### * : For these methods the output may differ base on the arrangement of the states.

##### FSA.remove_state(self, state)
Removes a state from the fsa. This includes removing the given state from the set of initial states, the set of final states, and the set of transition relations.
```
fsa.STATES returns {"X", "Y", "Z"}
fsa.TRANSITIONS 
    returns {   'X': {'Y': {'a'}},
                'Y': {'Z': {'b'}},
                'Z': {'X': {'a'}} }
fsa.INITIAL = {"X"}
fsa.remove_state("X")

fsa.STATES returns {"Y", "Z"}
fsa.TRANSITIONS 
    returns {   'Y': {'Z': {'b'}},
                'Z': {}
fsa.INITIAL = {}
```


##### FSA.remove_initial_state(self, state)
Removes a state from the set of initial states.
```
fsa.INITIAL = {"X"}

fsa.remove_initial_state("A")
fsa.INITIAL = {"X"} # Note that nothing happens to INITIAL

fsa.remove_initial_state("X")
fsa.INITIAL = {}
```

##### FSA.remove_final_state(self, state)
Removes a state from the set of final states.
```
fsa.FINAL = {"Y"}

fsa.remove_final_state("A")
fsa.FINAL = {"Y"} # Note that nothing happens to FINAL

fsa.remove_final_state("Y")
fsa.FINAL = {}
```

##### FSA.remove_transition(self, current_state, label, new_state)
Removes a transition from the set of transition relations. 
```
fsa.TRANSITIONS 
    returns {   'X': {'Y': {'a'}},
                'Y': {'Z': {'b'}},
                'Z': {'X': {'a'}} }
fsa.remove_transition("X", "a", "Z") 
fsa.TRANSITIONS # Note that nothing happens to TRANSITIONS
    returns {   'X': {'Y': {'a'}},
                'Y': {'Z': {'b'}},
                'Z': {'X': {'a'}} } 
fsa.remove_transition("Z", "a", "X") 
fsa.TRANSITIONS 
    returns {   'X': {'Y': {'a'}},
                'Y': {'Z': {'b'}} }
```

## Problems Encountered and Solutions
#### Adding new states
Initially, I stored my transition relations in a 2D array that resemble a adjacency matrix. There were a lot of problems as a result of this decision. These include taking up O(n^2) space, a dictionary/list to maintain which row/column represents which state, and resizing array to add states. 

Solution: I switch to using a dictionary to store my transition relations. This easily solve the issue of keep track of which row/column is which state, since the keys can be a state. In addition, this also resolve the issue with resizing and space. Since, it is a dictionary it does not have to initialize a spot for every possible transition relation in the fsa and only maintain the existing transition relations. 

#### Testing with an empty FSA.
Putting this inside a test method results in weird actions that I don't understand why it is occurring. Might have something to do with default values possibly?
```
tester = FSA()
```
Solution: At first, I made a seperate method call empty() that just returns FSA(set(), set(), []). I could have probably just done this in the test method rather than make an additional method. However, later on I switch to testing with a randomly generated fsa which did not have this issue appear.

#### How to test the get methods? 
Solution: Since testing the methods with unit tests wouldn't be effective as it will be the same as rewriting the method in the unit test, I decided to test those methods with an example that can be verify by looking at the code rather than try to do an elaborate way of predicting the result since sets are not ordered.

## Short run through/How to use
This is the driver.py file
```
# To define your FSA

# You can play around with these variables. 
# Note I and F should be a set and T is an array of tuples of the form (current_state, label, next_state)
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
    
# You can also try the under methods to manipulate your fsa without having to change the variables are the start


# Interactive way through the terminal to manipulate your fsa
This is a sample run:
What do you to do:
Add     [A/add]
Matrix  [M/matrix]
Remove  [R/remove]
View    [V/view]
[C/clear] to clear the screen
[Q/quit] to quit
$ A

What do you want to add:
1. Final state [F/final]
2. Inital state[I/initial]
3. A new state [S/state]
4. A transition[T/transition]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ S
Enter the state: W

What do you want to add:
1. Final state [F/final]
2. Inital state[I/initial]
3. A new state [S/state]
4. A transition[T/transition]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ b

What do you to do:
Add     [A/add]
Matrix  [M/matrix]
Remove  [R/remove]
View    [V/view]
[C/clear] to clear the screen
[Q/quit] to quit
$ V

What do you want to view:
1. Final states [F/final]
2. Inital states[I/initial]
3. states       [S/state]
4. Transitions  [T/transition]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ S
{'Y', 'W', 'X', 'Z'}

What do you want to view:
1. Final states [F/final]
2. Inital states[I/initial]
3. states       [S/state]
4. Transitions  [T/transition]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ b

What do you to do:
Add     [A/add]
Matrix  [M/matrix]
Remove  [R/remove]
View    [V/view]
[C/clear] to clear the screen
[Q/quit] to quit
$ M

What do you want to view:
1. Final matrix [F/final]
2. Inital matrix[I/initial]
3. Letter matrix[L/letter]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ I
[0 0 1 0]

What do you want to view:
1. Final matrix [F/final]
2. Inital matrix[I/initial]
3. Letter matrix[L/letter]
[B/back] to get back to the main menu
[C/clear] to clear the screen
[Q/quit] to quit
$ 

You can try other methods by reading the instruction after running the driver file.
Note: Quiting does not save your fsa in it's new state
```

#### This is a note for makefile
```
This runs the example
$ make
python driver.py 

This runs the test file
$ make test
python -m pytest testFSA.py # for unit tests
python testFSA.py # for the getters
```
