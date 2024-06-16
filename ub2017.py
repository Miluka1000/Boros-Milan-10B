class Ultra:
    def __init__(self,sor):
        adatok = sor.strip().split(";")
        self.versenyto = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.idoeredmeny = adatok[3]
        self.tavszazalek = int(adatok[4])
        ido = adatok[3].split(":")
        self.ora = int(ido[0])
        self.perc = int(ido[1])
        self.ms = int(ido[2])
        self.osszora = self.ora + self.perc / 60 + self.ms/3600

ub:list[Ultra] = []
file = open("ub2017egyeni.txt","r")
fejlec = file.readline()
for sor in file:
    ub.append(Ultra(sor))
file.close()

print(f"3.2 feladat: Futók száma: {len(ub)}")

#megszámlálás és
db = 0
for i in ub:
    if i.tavszazalek == 100 and i.kategoria == "Noi":
        db += 1
print(f"3.3 feladat: Célba érkező női sportoló: {db} fő.")

#maximumkeresés tétele
max_hossz = 0
max_index = 0
for i in range(len(ub)):
    if len(ub[i].versenyto) > max_hossz:
        max_hossz = len(ub[i].versenyto)
        max_index = i
print("3.4 feladat: A leghosszabb nevő futó:")
print(f"\tNév: {ub[max_index].versenyto}")
print(f"\tRajtszáma: {ub[max_index].rajtszam}")
print(f"\tEredmény: {ub[max_index].idoeredmeny}")

ossz_ido = 0
db = 0
for i in ub:
    if i.kategoria == "Ferfi" and i.tavszazalek == 100:
        ossz_ido += i.osszora
        db += 1
print(f"3.5 feladat: Férfi sportolók átlagos ideje: {ossz_ido/db} óra")