
def pivot(posh,posv, string,plateau):
        decH=abs(posh-8)
        decV=abs(posv-8)
        plateau[(8+decH,8+decV)]=["  #  ",string]
        plateau[(8-decH,8+decV)]=["  #  ",string]
        plateau[(8+decH,8-decV)]=["  #  ",string]
        plateau[(8-decH,8-decV)]=["  #  ",string]

def creation_plateau():
#création du plateau de scrabble
#première coordonnée indique la ligne horizontale tandis que la deuxième indique la ligne verticale
        plateau={}
        for i in range(1,16):
                for j in range(1,16):
                        plateau[(i,j)]=["  #  ","   "]

#mots compte triple
        pivot(1,1,"MCT",plateau)
        pivot(1,8,"MCT",plateau)
#mots compte double
        pivot(8,8,"MCD",plateau)
        for i in range(2,5):
                pivot(i,i,"MCD",plateau)
#lettre compte double
        pivot(7,7,"LCD",plateau)
        pivot(8,4,"LCD",plateau)
        pivot(4,8,"LCD",plateau)
        pivot(7,3,"LCD",plateau)
        pivot(4,1,"LCD",plateau)
        pivot(1,4,"LCD",plateau)
        pivot(3,7,"LCD",plateau)
#lettre compte triple
        pivot(2,6,"LCT",plateau)
        pivot(6,2,"LCT",plateau)
        pivot(6,6,"LCT",plateau)
        return plateau

def affichageplateau(plateau):
        ligne='      '
        remplissage='    '
        for i in range(1,16):
                remplissage=remplissage+' ___  '


        for i in range(1,16):
                if i<=9:
                        ligne=ligne+str(i)+'     '
                else:
                        ligne=ligne+str(i)+'    '
        print(ligne)
        for i in range(1,16):
                if i<=9:
                        ligne='  '+str(i)+'|'
                else:
                        ligne=' '+str(i)+'|'
                for j in range(1,16):
                        a=plateau[(i,j)]
                        
                        ligne=ligne+' '+str(a[1])+" |"
                        
                print(remplissage)
                print()     
                print(ligne)
        print(remplissage)


plateau=creation_plateau()
affichageplateau(plateau)






