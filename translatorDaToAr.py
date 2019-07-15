import pyarabic.araby as araby
import json
from pyarabic.unshape import unshaping_line
import arabic_reshaper
def correctionSequence(tableau,sequence):
    print(tableau)
    Asup = []
    for x in range(0,len(tableau)-1):
        i=x
        j=i+1
        if tableau[i] == tableau[j][0]:
            Asup.append(i)
    i=0
    for y in Asup:
        tableau.pop(y-i)
        sequence.pop(y-i)
        i=i+1

    # print(tableau)
    for x in range(0,len(tableau)-3):
        if tableau[x]!=" ":
            if tableau[x][1:] != "":
                if len(tableau[x+1]) >=1 :
                    if tableau[x][1:] in tableau[x+1]:
                        tableau.pop(x+1)
                        sequence.pop(x+1)
    print(tableau)
    # assert arabic_reshaper.reshape('ر ي ت و ي ت'.replace(' ', '')) == 'ﺭ ﻳ ﺘ ﻮ ﻳ ﺖ'.replace(' ', '')
    # assert arabic_reshaper.reshape('ر ي ت و ي ت'.replace(' ', '')) == '\ufead \ufef3 \ufe98 \ufeee \ufef3 \ufe96'.replace(' ', '')
    fichier = open("data.txt", "w")
    for end in sequence:
        fichier.write(end)
        if end=='':
            fichier.write('\n')
    fichier.close()
    # print(arabic_reshaper.reshape(motfin.replace(' ', '')))
    # print(arabic_reshaper.reshape('ر ي ت و ي ب'.replace(' ', '')))
    


sequence = []
motAdd = []
with open('synonime.json') as json_file:  
    motT="bbrit nsifet lflous lkhouya f hind"
    print(motT)
    i =0
    data = json.load(json_file)
    breaker = False
    for lettre in motT:
        j=i+1
        while j<=len(motT):
            t=0
            for parse in data:
                breaker = False
                for x in data[parse]:
                    if motT[i:j] in x['translate']:
                        if t==1:
                            print("pop")
                            sequence.pop()
                        t=1
                        sequence.append(parse)
                        motAdd.append(motT[i:j])
                    else:
                        if t==1:
                            breaker = True
                            break 
                if breaker :
                    
                    break
            j=j+1
        i=i+1
    

correctionSequence(motAdd,sequence)
