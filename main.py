import pyarabic.araby as araby
import json

with open('synonime.json') as json_file:  
    motT="khalini"
    i =0
    data = json.load(json_file)
    sequence = []
    motAdd = []
    for lettre in motT:
        j=0
        while j<len(motT):
            for parse1 in data:
                for parse in data:
                    t=0
                    for x in data[parse]:
                        if motT[i:j] in x['translate']:
                            motAdd.append(motT[i:j])
                            sequence.append(parse)
                            t=1
                            i=j
                            break
                j=j+1
        j=i
        i=i+1 
    print(sequence)