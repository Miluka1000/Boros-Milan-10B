#lista elemeinek összegét adja visza

import random
szamok = []
for i in range(10):
    szamok.append(random.randint(10,99))
print(szamok)  
    
osszeg = 0
for i in szamok:
    osszeg += i
print(osszeg)