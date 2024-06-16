#bizonyos elemeket számol meg a listában
#pl.: -10 - 10 közötti számokkal töltünk ki listákat, feladat
#hány 0-nál kisebb, hány 0-nál nagyobb számot tartalmaz.

import random
szamok = []
for i in range(10):
    vsz = random.randint(-10,10)
    while vsz == 0:
        vsz = random.randint(-10,10)
    szamok.append(vsz)
print(szamok)

pozitiv = 0
for i in szamok:
    if i > 0:
        pozitiv += 1
print(f"Pozitív számok {pozitiv} db, negatív számok {len(szamok)-pozitiv} db.")
