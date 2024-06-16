#ugyanaz, mint a eldöntés tétele, de azt is keressük, hogy a megtalált
#elem hányadik 

import random
szamok = []
for i in range(10):
    szamok.append(random.randint(10,99))
print(szamok)  

van = False
hely = 0
for i in range(len(szamok)):
    if szamok[i] % 3 == 0:
        van = True
        hely = i
        break
if van:
    print("Van a listában hárommal osztható szám.")
    print(f"Az első szám a listából, ami osztható hárommal: {hely+1}. szám: {szamok[hely]}")
else:
    print("Nincs a listában hárommal osztható szám.")