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
* Numpy - For matrix multiplication

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
    This is the format for how the dictionary should look like with s0,s1,...,sn representing the states and arc_label is a single letter alphabetic character 
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
MEM_LETTER:  The dictionary containing the boolean letter matrices that have already been used for memoization
```




## Problems Encountered and Solutions


## Short run through 
