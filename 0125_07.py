szam = int(input("Kérem adjon meg egy számot 1 és 10 között: "))
if szam > 10:
    print("Nem jó számot adtál meg.")
print("Szorzás:")
for i in range(11):
    print(f"{szam} * {i}={szam * i}")
    
print("Hatvány:")
for i in range(11):
    print(f"{szam} ^ {i}={szam ** i}")