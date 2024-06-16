#azt vizsgájuk, hogy szerepel-e egy bizonyos tulajdonságú elem a listában
#keresést csak addig folytatjuk amíg bíztosan el nem tudjuk dönteni a választ
#pl.: van-e 3-mal ösztható szám a listában?

import random
szamok = []
for i in range(10):
    szamok.append(random.randint(10,99))
print(szamok)  

van = False
for i in szamok:
    if i % 3 == 0:
        van = True
        break
if van:
    print("Van a listában hárommal osztható szám.")
else:
    print("Nincs a listában hárommal osztható szám.")