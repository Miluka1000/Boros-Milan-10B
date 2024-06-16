class Nobel:
    def __init__(self,sor):
        adatok = sor.strip().split(";")
        self.ev = int(adatok[0])
        self.tipus = adatok[1]
        self.knev = adatok[2]
        self.vnev = adatok[3]
        
nobel:list[Nobel] = []
file = open("nobel.csv","r",encoding="utf-8")
fejlec = file.readline()
for sor in file:
    nobel.append(Nobel(sor))
file.close()

for i in nobel:
    if i.knev == "Arthur B." and i.vnev == "McDonald":
        print(f"3. feladat: {i.tipus}")

for i in range(len(nobel)):
    if nobel[i].ev == 2017 and nobel[i].tipus == "irodalmi":
        print(f"4. feladat: {nobel[i].knev} {nobel[i].vnev}")
        
print("5. feladat: ")
for i in nobel:
    if i.ev > 1990 and i.tipus == "béke" and i.vnev == "":
        print(f"\t{i.ev}: {i.knev}")
        
print("6. feladat:")
for i in nobel:
    if "Curie" in i.vnev:
        print(f"\t{i.ev}: {i.knev} {i.vnev} ({i.tipus})")
        
print("7. feladat:")
szotar = {}
for i in nobel:
    if i.tipus not in szotar:
        szotar[i.tipus] = 1
    else:
        szotar[i.tipus] += 1
for k,v in szotar.items():
    print(f"\t{k} - {v}")
    
print("8. feladat:")
file = open("orvosi.txt","w",encoding="utf-8")
for i in range(len(nobel)):
    if nobel[i].tipus == "orvosi":
        file.write(f"{nobel[i].ev} : {nobel[i].knev} {nobel[i].vnev}\n")