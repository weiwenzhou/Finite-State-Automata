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

## Implementation


## Problems Encountered and Solutions


## Short run through 
