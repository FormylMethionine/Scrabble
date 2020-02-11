from randstring import generateBag, tirage, randstring
import time


def list_from_file(name):

    with open(name, "r") as f:
        liste = f.read()
        liste = liste.split()

    return liste


def regroup(listOfWords, i):

    dic = {}
    for word in listOfWords:
        if i >= len(word):
            dic[0] = word
        elif word[i] not in dic:
            dic[word[i]] = [word]
        else:
            dic[word[i]].append(word)

    return dic


def make_dic(liste, i):

    ret = liste

    ret = regroup(ret, i)
    i += 1
    for letter in ret:
        if type(letter) != int:
            ret[letter] = make_dic(ret[letter], i)

    return ret


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


def search_dic(dic, letters, base=""):

    for letter in base:
        dic = dic[letter]

    letters = permutlist(letters)
    ret = set()
    # print(letters)
    for word in letters:
        srcdic = {i: dic[i] for i in dic}
        for letter in word:
            # penser à ajouter gestions des jokers:
            # if letter==joker:
            #   for i in "alphabet":
            #       search
            if 0 in srcdic and srcdic[0] not in ret:
                ret.add(srcdic[0])
            if letter in srcdic:
                srcdic = srcdic[letter]

    return ret


def rec_search_word(dic, word, ret):

    if 0 in dic and dic[0] not in ret:
        ret.add(dic[0])

    if word[0] == "1":
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if letter in dic:
                rec_search_word(dic[letter], word[1:], ret)

    elif word[0] in dic:
        rec_search_word(dic[word[0]], word[1:], ret)


def rec_search_dic(dic, letters, base=""):

    letters = permutlist(letters)
    if base != "":
        for letter in base:
            dic = dic[letter]

    ret = set()
    for word in letters:
        rec_search_word(dic, word, ret)

    return ret


t0 = time.perf_counter()
liste = list_from_file("liste.txt")
print(len(liste))
dic = (make_dic(liste, 0))
bag = generateBag()
letters, bag = tirage(bag, 7)
print(letters)
playable = (rec_search_dic(dic, letters))
t1 = time.perf_counter()
print(playable, len(playable))
print(t1-t0)
