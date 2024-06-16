class Hegyek:
    def __init__(self,sor):
        #sor = "Ágasvár;Mátra;789"
        adatok = sor.strip().split(";")
        #adatok[0] = "Ágasvár"  adatok[1] = "Mátra"  adatok[2] = "789"
        self.hegycsucs = adatok[0]
        self.hegyseg = adatok[1]
        self.magassag = int(adatok[2])
    
hegy:list[Hegyek] = []
file = open("Magyarorszag_hegyek.txt","r",encoding="utf-8")
fejlec = file.readline()
for sor in file:
    hegy.append(Hegyek(sor))
file.close()

print(f"3. feladat: Hegycsúcsok száma: {len(hegy)} db")

#megszámlálás tétele
ossz_mag = 0
for i in hegy:
    ossz_mag += i.magassag
print(f"4. feladat: Hegycsúcsok átlagos magassága: {ossz_mag/len(hegy)} m.")

#maximumkeresés tétele
max_mag = 0
max_index = 0
for i in range(len(hegy)):
    if hegy[i].magassag > max_mag:
        max_mag = hegy[i].magassag
        max_index = i
print(f"5. feladat: A legmagassabb hegycsúcs adatai:")
print(f"\tNév: {hegy[max_index].hegycsucs}")
print(f"\tHegység: {hegy[max_index].hegyseg}")
print(f"\tMagasság: {hegy[max_index].magassag} m")

#eldöntés tétele
be_mag = int(input("6. feladat: Kérek egy magassgot: "))
van = False
for i in hegy:
    if i.magassag > be_mag and i.hegyseg == "Börzsöny":
        van =  True
        break
if van == True:
    print(f"\tVan ",end="")
else:
    print(f"Nincs ",end="")
print(f"{be_mag}m-nél magasabb hegycsúcs a Börzsönsben.")

#kiválogatás tétele
v = 3.280839895
db = 0
for i in hegy:
    if i.magassag*v > 3000:
        db += 1
print(f"7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {db}")

print("8. feladat: Statisztika")
szotar = {}
for i in hegy:
    if i.hegyseg not in szotar:
        szotar[i.hegyseg] = 1
    else:
        szotar[i.hegyseg] += 1
for k,v in szotar.items():
    print(f"\t{k} - {v} db")

print("9. feladat: bukk_vidék.txt")
v = 3.280839895
file = open("bukk_videk.txt","w",encoding="utf-8")
file.write("Hegycsúcs neve;Magasság láb\n")
for i in hegy:
    if i.hegyseg == "Bükk-vidék":
        file.write(f"{i.hegycsucs};{i.hegyseg};{i.magassag*v:.1f}\n")
file.close()