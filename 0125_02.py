import random
import math

szamok = []
for i in range(3):
    szamok.append(random.randint(1,10))
szorzat = 1
for i in szamok:
    szorzat *= i      #szorzat = szorzat * i
    
print(f"A számok szorzata: {szorzat}")
print(f"Az összeg gyöke: {math.sqrt(szorzat)}")


print(math.pow(3,2))




gyümölcs=["körte","banán","alma","citrom","dinnye"]
print(random.choice(gyümölcs))

print("Lottó számok:",end="")
szam = []
for i in range(5):  #0-lától kezdődik (0,1,2,3,4)
    vsz = random.randint(1,90)
    while vsz in szam:
        vsz = random.randint(1,90)
    szam.append(vsz)
szam.sort()
print(*szam,sep=" ")

gyümölcs.sort()
print(*gyümölcs,sep=" ")

print(random.randrange(100,1000,2))

print(random.uniform(1.3,2.8))
