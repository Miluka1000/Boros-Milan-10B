#két tömbe válogatjuk szét a lista elemeit
#pl.: 45, és az alattiak és 45 felettiek

import random
szamok = []
for i in range(10):
    szamok.append(random.randint(10,99))
    szamok.sort()
print(szamok)  

jszamok = []
rszamok = []
for i in szamok:
    if i <= 45:
        jszamok.append(i)
    else:
        rszamok.append(i)
print(f"Kisebbek: {jszamok}")
print(f"Nagyobbak: {rszamok}")