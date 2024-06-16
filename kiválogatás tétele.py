#egy lista elemeit átrakom egy másik listába, ha megfelelnek egy adott feltételnek
#pl.: 25 vagy annál kisebb számokat rakjuk át

import random
szamok = []
for i in range(10):
    szamok.append(random.randint(10,99))
szamok.sort()
print(szamok)  

ujlista = []
for i in szamok:
    if i < 25:
        ujlista.append(i)
print(ujlista)