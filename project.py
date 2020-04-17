fsa = {"I": 1,
       "F": 2,
       "T": {0: {"a": 1, "a": 2},
             1: {"a": 2},
             2: {"b": 3},
             3: {"a": 1}
            }
      }

fsa1 = {"I": 0,
       "F": {3},
       "T": {0: {"a": {1, 2} },
             1: {"c": {1}, "b": {2}, "c": {3}  },
             2: {"b": {2}, "a": {3}}
            }
       }

fsaT = {"I": 0,
       "F": {3},
       "T": { (0, "a", 1),
              (0, "a", 2),
              (1, "c", 1),
              (1, "b", 2),
              (1, "c", 3),
              (2, "b", 2),
              (2, "a", 3)
            }
       }


def convertFsaToMatrix(fsa):
    """ Returns the Boolean matrix representation of a FSA.

    The FSA must be a dictionary of the form
    {'I': initial_state,
     'F': {final_state1, final_state2, ...},
     'T': {edge1, edge2, ...}}
     edge : (current_state, letter, next_state)

     # {current_state: {word: next_state}}

    Arguments
    ---------
    fsa: dict
        finite-state automaton

    Returns
    -------
    dict
    """
    # the list of all states in the fsa
    states = {k:i for i, k in enumerate(list({k[i] for i in [0,2] for k in fsa.get('T')}))}
    print(states)
    letters = list({k[1] for k in fsa.get('T')})
    letters.sort()
    print(letters)
    repr = {};
    # initial_state matrix
    repr['I'] = [1 if k == fsa.get('I') else 0 for k in states]
    # final_state matrix
    repr['F'] = [1 if k in fsa.get('F') else 0 for k in states]
    # matrix of adjacency edges
    adj = [[0 for i in states] for j in states]
    for c, l, n in fsa.get('T'):
        adj[states[c]][states[n]] = l
    print_matrix(adj)
    # dictionary of transition matrice
    # repr['T'] = {k: for k in letters}
    repr['T'] = {}
    for k in letters:
        temp = [[1 if k == next else 0 for next in matrix] for matrix in adj]
        repr['T'][k] = temp
        print(k)
        print_matrix(temp)
    # print(repr)

def print_matrix(matrix):
    for x in matrix:
        print(x)
    print()

matrixRepr = convertFsaToMatrix(fsaT)

def accepts(word, fsa_matrix):
    """Test if FSA accepts the word.

    Arguments
    ---------
    sentence: string
        word
    fsa: dict
        finite-state automaton

    Returns
    -------
    bool
    """
    result = fsa_matrix['I']
    for letter in word:
        m = fsa_matrix['T'].get(letter)
        if m:
            print("Letter doesn't exist")
            return False

def matrix_multiplication(m1, m2):
    """ Return the matrix product of two matrices. m1*m2

    Arguments
    ---------
    m1 : m by n matrix
        matrix 1
    m2 : n by p matrix
        matrix 2

    Returns
    -------
    m by p matrix
    """
    m = len(m1)
    n = len(m1[0])
    if n != len(m2):
        raise ValueError("Dimensions for the matrices do not match.")
    p = len(m2[0])

    result = []
    for i in range(m):
        row = []
        for j in range(p):
            sum = 0
            for k in range(p):
                sum += m1[i][k] * m2[k][j]
            if sum > 0:
                sum = 1
            row.append(sum)
        result.append(row)

    return result

m1 = [[0,1], [1,1]]
m2 = [[1], [1]]

print_matrix(matrix_multiplication(m1, m2))
