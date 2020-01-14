def score(string):

    score=0

    for letter in string:
       
        if letter=='A':
            score+=1
        elif letter=='B':
            score+=3
        elif letter=='C':
            score+=3
        elif letter=='D':
            score+=2
        elif letter=='E':
            score+=1
        elif letter=='F':
            score+=4
        elif letter=='G':
            score+=2
        elif letter=='H':
            score+=4
        elif letter=='I':
            score+=1
        elif letter=='J':
            score+=8
        elif letter=='K':
            score+=10
        elif letter=='L':
            score+=1
        elif letter=='M':
            score+=2
        elif letter=='N':
            score+=1
        elif letter=='O':
            score+=1
        elif letter=='P':
            score+=3
        elif letter=='Q':
            score+=8
        elif letter=='R':
            score+=1
        elif letter=='S':
            score+=1
        elif letter=='T':
            score+=1
        elif letter=='U':
            score+=1
        elif letter=='V':
            score+=4
        elif letter=='W':
            score+=10
        elif letter=='X':
            score+=10
        elif letter=='Y':
            score+=10
        elif letter=='Z':
            score+=10
        elif letter=='1':  #joker (en attendant d'enlever le else suivant)
            score+=0
        else: #check les erreurs dans la string, utile pour vérifier le tirage, à retirer dans la VF
            print("wtf bro")
            break;

    return score

print(score("YEUX"))
