#ha tudjuk, hogy a keresett értéket a lista tartalmazza
#pl.: hol áll a listában a 4-es szám

szamok = [1,5,3,8,9,4,2,7,6]

i = 0
while szamok[i] != 4:
    i += 1
print(f"A 4-es szám a(z) {i+1}. elem a listában.")