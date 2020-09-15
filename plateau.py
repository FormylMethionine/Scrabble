
def pivot(posh,posv,string,plateau):
        decH=abs(posh-8)
        decV=abs(posv-8)
        plateau[(8+decH,8+decV)]=[" ",string]
        plateau[(8-decH,8+decV)]=[" ",string]
        plateau[(8+decH,8-decV)]=[" ",string]
        plateau[(8-decH,8-decV)]=[" ",string]

def creation_plateau():
#création du plateau de scrabble
#première coordonnée indique la ligne horizontale tandis que la deuxième indique la ligne verticale
        plateau={}
        for i in range(1,16):
                for j in range(1,16):
                        plateau[(i,j)]=[" ","   "]

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

def affichageplateau_bonus(plateau):
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

def affichageplateau_lettres(plateau):
        ligne='       '
        remplissage='    '
        for i in range(1,16):
                remplissage=remplissage+'  ___   '


        for i in range(1,16):
                if i<=9:
                        ligne=ligne+str(i)+'       '
                else:
                        ligne=ligne+str(i)+'      '
        print(ligne)
        for i in range(1,16):
                if i<=9:
                        ligne='  '+str(i)+'|'
                else:
                        ligne=' '+str(i)+'|'
                for j in range(1,16):
                        a=plateau[(i,j)]
                        
                        ligne=ligne+'   '+str(a[0])+"   |"
                        
                print(remplissage)
                print()     
                print(ligne)
        print(remplissage)

def place_mot(mot, pos,sens,plateau):
    if sens=='H':
        i=0
        for lettre in mot:
            plateau[(pos[0],pos[1]+i)]=lettre
            i=i+1                               
    elif sens=='V':
        i=0
        for lettre in mot:
            plateau[(pos[0]+i,pos[1])]=lettre
            i=i+1
    return 0;

def plateau_rempli():
    
    plto=creation_plateau()
    place_mot('BIZARRE',(1,1),'H',plto)
    place_mot('DESOLER',(2,2),'H',plto)#ok
    place_mot('VAR',(3,9),'H',plto) #ok 
    place_mot('MELIONS',(4,3),'H',plto) #ok
    place_mot('EWE',(4,11),'H',plto) #ok
    place_mot('KAPPA',(6,9),'H',plto)#ok
    place_mot('HI',(7,8),'H',plto)#ok
    place_mot('YUE',(7,13),'H',plto)#ok
    place_mot('CAFES',(8,7),'H',plto)#ok
    place_mot('ETAIERA',(9,1),'H',plto)
    place_mot('LIMITONS',(12,4),'H',plto)#ok
    place_mot('EUE',(13,1),'H',plto)#ok
    place_mot('SAMOANE',(14,3),'H',plto)#ok
    place_mot('SOIF',(15,7),'H',plto)#ok
   
    place_mot('TENDUE',(8,1),'V',plto) #ok
    place_mot('LEVITERAI',(4,5),'V',plto) #ok
    place_mot('EGO',(2,7),'V',plto)#ok
    place_mot('CA',(8,7),'V',plto)#ok
    place_mot('AS',(14,7),'V',plto)#ok
    place_mot('HA',(7,8),'V',plto)#ok
    place_mot('NO',(14,8),'V',plto)#ok
    place_mot('VS',(3,9),'V',plto)#ok
    place_mot('KIF',(6,9),'V',plto)#ok
    place_mot('EI',(14,9),'V',plto)        
    place_mot('ZEN',(10,10),'V',plto)#ok
    place_mot('RE',(3,11),'V',plto)#ok
    place_mot('DELAYER',(3,13),'V',plto)#ok
    place_mot('LUXER',(4,15),'V',plto)#ok
    
    return plto


def mots_plateau(plateau):
    mots=[]	
#parcours vertical et horizontal du plateau     
    for i in range(1,16):
        lignev=['Ve']
        ligneh=['He']
#suppression de certains espaces vides
        for j in range(1,16):
            
            if j==1:
                if plateau[(j+1,i)][0]==' ':
                    a='bof'
                else:
                    lignev.append(    [plateau[(j,i)][0] ,  (j,i)]    )
                
                if plateau[(i,j+1)][0]==' ':
                    a='bof'
                else:
                    ligneh.append(    [plateau[(i,j)][0] ,  (i,j)]    )                
                 

            if j<15 and j>1:
                if plateau[(j-1,i)][0]==' ' and plateau[(j+1,i)][0]==' ': 
                    a='bof'
                else:
                    lignev.append(    [plateau[(j,i)][0] ,  (j,i)]    )

                if plateau[(i,j-1)][0]==' ' and plateau[(i,j+1)][0]==' ':
 
                    a='bof'
                else:
                    ligneh.append(    [plateau[(i,j)][0] ,  (i,j)]    )

            if j==15:
                if plateau[(j-1,i)][0]==' ':
                    a='bof'
                else:
                    lignev.append(    [plateau[(j,i)][0] ,  (j,i)]    )
                
                if plateau[(i,j-1)][0]==' ':
                    a='bof'
                else:
                    ligneh.append(    [plateau[(i,j)][0] ,  (i,j)]    )                
       
        
        mots.append(lignev)
        mots.append(ligneh)
        
    rep=[]
    mot=""
    pos=""
    compt=0
    coord=(0,0)
    for ligne in mots:
        if ligne==['Ve'] or ligne==['He']:
            continue
        
        
        elif ligne[0]=='Ve':
            pos='V'
        elif ligne[0]=='He':
            pos='H'	
        for element in ligne: 
            if element=='Ve' or element=='He':
                continue
            if element[0]==' ':
                compt=0
            elif element[0]!=' ' and compt==0:
                mot=element[0]
                coord=element[1]
                compt=compt+1


            elif element[0]!=' ':
                mot=mot+element[0]
                compt=compt+1
            
            if compt==0 and mot!="":
                rep.append([pos,coord,mot])
                mot=""
        if mot!="":
            rep.append([pos,coord,mot])
            mot=""         
    return rep


a=plateau_rempli()
affichageplateau_lettres(a)
print(mots_plateau(a))        










