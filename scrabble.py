from randstring import generateBag, tirage, randstring
from calculateScore import score
import time


def list_from_file(name):

    with open(name, "r") as f:
        liste = f.read()
        liste = liste.split()

    return liste

#A partir d'une liste de mots, on les compartimente en fonction d'une lettre à une place donnée.
def regroup(listOfWords, i):
    dic = {}
    for word in listOfWords:
#si le mot a la même longueur que l'indice, il est complètement décrit. La clé 0 indique que le chemin pour le trouver est complété.
        if i >= len(word):
            dic[0] = word
#Si la clé-lettre word[i] n'existe pas, on l'ajoute et on y associe le mot.
        elif word[i] not in dic:
            dic[word[i]] = [word]
#Si la clé-lettre existe déjà, on ajoute le mot à la liste de mots existants, associée à la même série de clés.
        else:
            dic[word[i]].append(word)

    return dic

#crée un dictionnaire
def make_dic(liste, i):
#ret est la liste de mots initiale.
#plus tard, ret devient une liste de mots associée à une clé. 
    ret = liste
#premier tour, ret est devenu un dictionnaire
    ret = regroup(ret, i)
    i += 1
#ret est devenu un dictionnaire, on va parcourir toutes les clés possibles. 
    for letter in ret:
        if type(letter) != int:
#On crée un dictionnaire dans un dictionnaire, jusqu'à ce que tous les chemins soient parcourus et que toutes les clés des dictionnaires se terminent par 0.
            ret[letter] = make_dic(ret[letter], i)

    return ret

#retourne une liste avec toutes les permutations possibles de la chaîne de caractères indiquée.
def permutlist(string):

    p = [[c for c in string]]
    ret = set()
    ret.add(string)

    for k in range(len(string)-1):
        for i in range(len(p)):
            perm = p[i][:]
            for j in range(len(string)-k-1):
                perm.append(perm.pop(k))
                p.append(perm[:])

    for i in p:
        string = ""
        for j in i:
            string += j
        if string not in ret:
            ret.add(string)

    return ret

#paramètres utilisés : 
def search_word(dic, word, ret, retlist, i):

    jokers = []
    if 0 in dic and dic[0] not in ret:
        ret.add(dic[0])
        retlist.append((dic[0], jokers))

    if word != "":
        if word[0] == "1":
            jokers.append(i)
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if letter in dic:
                    i += 1
                    search_word(dic[letter], word[1:], ret, retlist, i)

        elif word[0] in dic:
            i += 1
            search_word(dic[word[0]], word[1:], ret, retlist, i)


def search_dic(dic, letters, base=""):

    letters = permutlist(letters)
    if base != "":
        for letter in base:
            dic = dic[letter]
#ret est une liste vide.
    ret = set()
    wordlist = []
#pour chaque suite de lettres ordonnée différemment à chaque fois
    for word in letters:
        search_word(dic, word, ret, wordlist, len(base))

    return wordlist


def existence_mot(dic,letters):
        b=False
        ret=set()
        wordlist=[]
        search_word(dic, letters, ret, wordlist, 0)
        if len(wordlist)==1:
                if wordlist[0][0]==letters:
                        b=True
        elif len(wordlist)==0:
                b=False
        else:
                for word in wordlist:
                        if word==letters:
                                b=True
        return b




liste = list_from_file("liste.txt")
print(len(liste))
dic = (make_dic(liste, 0))
bag = generateBag()
letters, bag = tirage(bag, 7)
print(letters)
# un bug fonctionnait avec SAREGHN, RSCEIRH
a=existence_mot(dic,"TRANQUILLE")
print(a)
t0 = time.perf_counter()
playable = (search_dic(dic, letters))
t1 = time.perf_counter()
# playable = sorted(playable, key=score)[::-1]
print(playable, len(playable))
print(score(playable[1]))
print(t1-t0)
