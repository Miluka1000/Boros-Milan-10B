#minimumérték-kiválasztás / maximumérték-kiválasztás
#legkisebb és legnagyobb érték keresése a listában

import random
szamok = []
for i in range(10):
    szamok.append(random.randint(10,99))
print(szamok)  

min_szam = szamok[0]
max_szam = szamok[0]
for i in szamok:
    if i < min_szam:
        min_szam = i
    if i > max_szam:
        max_szam = i
print(f"Legkisebb elem: {min_szam}")
print(f"Legnagyobb elem: {max_szam}")