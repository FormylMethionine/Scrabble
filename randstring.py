import numpy as np

def randstring(n):
    
    string=""

    for i in range(n):

        tirage=np.random.randint(26)

        if tirage==0:
            string+="A"

        elif tirage==1:
            string+="B"

        elif tirage==2:
            string+="C"

        elif tirage==3:
            string+="D"

        elif tirage==4:
            string+="E"

        elif tirage==5:
            string+="F"

        elif tirage==6:
            string+="G"

        elif tirage==7:
            string+="H"

        elif tirage==8:
            string+="I"

        elif tirage==9:
            string+="J"

        elif tirage==10:
            string+="K"

        elif tirage==11:
            string+="L"

        elif tirage==12:
            string+="M"

        elif tirage==13:
            string+="N"

        elif tirage==14:
            string+="O"

        elif tirage==15:
            string+="P"

        elif tirage==16:
            string+="Q"

        elif tirage==17:
            string+="R"

        elif tirage==18:
            string+="S"

        elif tirage==19:
            string+="T"

        elif tirage==20:
            string+="U"

        elif tirage==21:
            string+="V"

        elif tirage==22:
            string+="W"

        elif tirage==23:
            string+="X"

        elif tirage==24:
            string+="Y"

        elif tirage==25:
            string+="Z"		
    
    return string
