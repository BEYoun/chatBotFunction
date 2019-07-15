from pyarabic.unshape import unshaping_line
import arabic_reshaper
from pyarabic import araby
f = open('data.txt','r')
lignes = f.readlines()
print(araby.vocalizedlike('ب ر ي ت'.replace(' ', ''), 'بريت'))
for ligne in lignes:
    f2 = open('right.txt','r')
    rights = f2.readlines()
    print(rights)
    for right in rights:
        if araby.vocalizedlike(unshaping_line(ligne).replace(' ', ''), unshaping_line(right)):
            print(unshaping_line(right).encode('utf8'))
            print('بريت')