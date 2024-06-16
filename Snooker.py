class Snooker:
    def __init__(self,sor):
        adatok = sor.strip().split(";")
        self.helyezes = adatok[0]
        self.nev = adatok[1]
        self.orszag = adatok[2]
        self.nyeremeny = int(adatok[3])

sno:list[Snooker] = []
file = open("snooker.txt","r")
fejlec = file.readline()
for sor in file:
    sno.append(Snooker(sor))
file.close()

print(f"3. feladat: A világranglistán {len(sno)} versenyző szerepel.")

#megszámlálás tétele
ossz_nyer = 0
for i in sno:
    ossz_nyer += i.nyeremeny
print(f"4. feladat: A versenyzők átlagosan {ossz_nyer/len(sno):.2f} fontot kerestek.")

#maximumkeresés tétele
max_nyer = 0
max_index = 0
for i in range(len(sno)):
    if sno[i].nyeremeny > max_nyer:
        max_nyer = sno[i].nyeremeny
        max_index = i
print("5. feladat: A legjobban kereső kínai versenyző:")
print(f"\tHelyezés: {sno[max_index].helyezes}")
print(f"\tNév: {sno[max_index].nev}")
print(f"\tOrszág: {sno[max_index].orszag}")
print(f"\tNyeremény összege: {sno[max_index].nyeremeny * 462.07:.0f} Ft")

van = False
for i in sno:
    if i.orszag == "Norvégia":
        van = True
        break
if van == True:
    print("6. feladat: versenyzők között van norvég versenyző.")
else:
    print("6. feladat: versenyzők között nincs norvég versenyző.")
    
print("7. feladat: Statisztika")
szotar = {}
for i in sno:
    if i.orszag not in szotar:
        szotar[i.orszag] = 1
    else:
        szotar[i.orszag] += 1
for k,v in szotar.items():
    if v > 4:
        print(f"\t{k} - {v} fő")