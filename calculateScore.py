def score(string):

    score = 0

    for letter in string:

        if letter == 'A':
            score += 1
        elif letter == 'B':
            score += 3
        elif letter == 'C':
            score += 3
        elif letter == 'D':
            score += 2
        elif letter == 'E':
            score += 1
        elif letter == 'F':
            score += 4
        elif letter == 'G':
            score += 2
        elif letter == 'H':
            score += 4
        elif letter == 'I':
            score += 1
        elif letter == 'J':
            score += 8
        elif letter == 'K':
            score += 10
        elif letter == 'L':
            score += 1
        elif letter == 'M':
            score += 2
        elif letter == 'N':
            score += 1
        elif letter == 'O':
            score += 1
        elif letter == 'P':
            score += 3
        elif letter == 'Q':
            score += 8
        elif letter == 'R':
            score += 1
        elif letter == 'S':
            score += 1
        elif letter == 'T':
            score += 1
        elif letter == 'U':
            score += 1
        elif letter == 'V':
            score += 4
        elif letter == 'W':
            score += 10
        elif letter == 'X':
            score += 10
        elif letter == 'Y':
            score += 10
        elif letter == 'Z':
            score += 10
        elif letter == '1':  # joker (en attendant d'enlever le else suivant)
            score += 0
        else:  # check les erreurs dans la string, utile pour vérifier le tirage, à retirer dans la VF
            print("wtf bro")
            break

    return score


def scoreFinal(string):

    score = 0
    table = {'A': 1,
             'B': 3,
             'C': 3,
             'D': 2,
             'E': 1,
             'F': 4,
             'G': 2,
             'H': 4,
             'I': 1,
             'J': 8,
             'K': 10,
             'L': 1,
             'M': 2,
             'N': 1,
             'O': 1,
             'P': 3,
             'Q': 8,
             'R': 1,
             'S': 1,
             'T': 1,
             'U': 1,
             'V': 4,
             'W': 10,
             'X': 10,
             'Y': 10,
             'Z': 10,
             '1': 0
             }

    for letter in string:
        if letter in table:
            score += table[letter]
        else:
            print("wtf bro")
            break

    return score


print(score("YEUX") == scoreFinal("YEUX"))
