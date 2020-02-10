import numpy as np


def randstring(n):

    string = ""

    for i in range(n):

        tirage = np.random.randint(26)

        if tirage == 0:
            string += "A"

        elif tirage == 1:
            string += "B"

        elif tirage == 2:
            string += "C"

        elif tirage == 3:
            string += "D"

        elif tirage == 4:
            string += "E"

        elif tirage == 5:
            string += "F"

        elif tirage == 6:
            string += "G"

        elif tirage == 7:
            string += "H"

        elif tirage == 8:
            string += "I"

        elif tirage == 9:
            string += "J"

        elif tirage == 10:
            string += "K"

        elif tirage == 11:
            string += "L"

        elif tirage == 12:
            string += "M"

        elif tirage == 13:
            string += "N"

        elif tirage == 14:
            string += "O"

        elif tirage == 15:
            string += "P"

        elif tirage == 16:
            string += "Q"

        elif tirage == 17:
            string += "R"

        elif tirage == 18:
            string += "S"

        elif tirage == 19:
            string += "T"

        elif tirage == 20:
            string += "U"

        elif tirage == 21:
            string += "V"

        elif tirage == 22:
            string += "W"

        elif tirage == 23:
            string += "X"

        elif tirage == 24:
            string += "Y"

        elif tirage == 25:
            string += "Z"

    return string


def Newrandstring(n):

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

    ret = []

    for i in range(9):
        ret += "A"
    for i in range(2):
        ret += "B"
    for i in range(2):
        ret += "C"
    for i in range(3):
        ret += "D"
    for i in range(15):
        ret += "E"
    for i in range(2):
        ret += "F"
    for i in range(2):
        ret += "G"
    for i in range(2):
        ret += "H"
    for i in range(8):
        ret += "I"
    for i in range(1):
        ret += "J"
    for i in range(1):
        ret += "K"
    for i in range(5):
        ret += "L"
    for i in range(3):
        ret += "M"
    for i in range(6):
        ret += "N"
    for i in range(6):
        ret += "O"
    for i in range(2):
        ret += "P"
    for i in range(1):
        ret += "Q"
    for i in range(6):
        ret += "R"
    for i in range(6):
        ret += "S"
    for i in range(6):
        ret += "T"
    for i in range(6):
        ret += "U"
    for i in range(2):
        ret += "V"
    for i in range(1):
        ret += "W"
    for i in range(1):
        ret += "X"
    for i in range(1):
        ret += "Y"
    for i in range(1):
        ret += "Z"
    for i in range(2):
        ret += "1"

    return ret


def NewgenerateBag():

    bag = []
    table = {

def tirage(liste, size):

    ret = ""

    for i in range(size):
        index = np.random.randint(len(liste))
        ret += liste.pop(index)

    return ret, liste
