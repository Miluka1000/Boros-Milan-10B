import random

def halmaze(lista):
    halmaz = set(lista)
    if len(halmaz) == len(lista):
        return True
    return False

print("2. feladat:")
for i in range(1,9):
    szamok = []
    for j in range(5):
        szamok.append(random.randint(1,9))
    if halmaze(szamok) == True:
        print(f"{i}. {szamok} -> Halmaznak tekinthaóető!")
    else:
        print(f"{i}. {szamok} -> Halmaznak nem tekinthető!")