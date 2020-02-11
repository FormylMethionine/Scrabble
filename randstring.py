import numpy as np


def randstring(n):

    string = ""
    table = {0: 'A',
             1: 'B',
             2: 'C',
             3: 'D',
             4: 'E',
             5: 'F',
             6: 'G',
             7: 'H',
             8: 'I',
             9: 'J',
             10: 'K',
             11: 'L',
             12: 'M',
             13: 'N',
             14: 'O',
             15: 'P',
             16: 'Q',
             17: 'R',
             18: 'S',
             19: 'T',
             20: 'U',
             21: 'V',
             22: 'W',
             23: 'X',
             24: 'Y',
             25: 'Z'
             }

    for i in range(n):

        tirage = np.random.randint(26)
        string += table[tirage]

    return string


def generateBag():

    bag = []
    table = {'A': 9,
             'B': 2,
             'C': 2,
             'D': 3,
             'E': 15,
             'F': 2,
             'G': 2,
             'H': 2,
             'I': 8,
             'J': 1,
             'K': 1,
             'L': 5,
             'M': 3,
             'N': 6,
             'O': 6,
             'P': 2,
             'Q': 1,
             'R': 6,
             'S': 6,
             'T': 6,
             'U': 6,
             'V': 2,
             'W': 1,
             'X': 1,
             'Y': 1,
             'Z': 1,
             '1': 2
             }

    for letter in table:
        for i in range(table[letter]):
            bag.append(letter)

    return bag


def tirage(liste, size):

    ret = ""

    for i in range(size):
        index = np.random.randint(len(liste))
        ret += liste.pop(index)

    return ret, liste
