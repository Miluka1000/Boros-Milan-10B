szam = input("Adjon meg egy 3 jegyű pozitív egész számot: ")   #pl.: 268 0-ik eleme: 2, 1. eleme:6 , 2. eleme:8 
egyesek = int(szam[2])
tizesek = int(szam[1])
százasok = int(szam[0])
# Négyzetre emelés: ^ vagy **
a = egyesek ** 3 + tizesek ** 3 + százasok ** 3
print(f"Eredeti szám: {szam} Százas: {százasok}  Tizes: {tizesek}  Egyes: {egyesek}")
if a == int(szam):
    print("A szám az Armstrong-szám.")
else:
    print("A szám az nem Armstrong-szám.")