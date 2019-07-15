import sys
from spellcheck import is_spelled_correctly
from eDist import func
wrong = []
values = sys.argv[1:]
#fichier = open("data.txt", "r")

for value in values:
    if not is_spelled_correctly(value):
        print("NOT SPELLED CORRECTLY: " + value)
        wrong.append(value)


newSentences = []
for word in values:
        if word in wrong:
                print(word)
                with open("spellWord.txt", "r") as fichier:
                        spellWord = fichier.read().split("\n")
                        newWord = []
                        for ligne in spellWord:
                                eDist=func(ligne,word)
                                if(eDist<=2):
                                        newWord.append(ligne)
                                        #print(newWord)
                        print(newWord)
                newSentences.append(newWord[0])                        
        else:
                newSentences.append(word)


print("La nouvelle phrase sans faute esttt ::::")

print(newSentences)

############################# TEST LIVENSHTEIN

# with open("data.txt", "r") as fichier:
#         for ligne in fichier.read().split("\n"):
#                 mots = ligne.split()
#                 eDist=func(mots[0],mots[1])
#                 print(eDist)
        