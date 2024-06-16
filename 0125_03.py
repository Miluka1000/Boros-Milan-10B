szamlalo = int(input("Add meg a számlálót: "))
nevezo =int(input("Add meg a nevezőt: "))

if szamlalo%nevezo == 0:
    print(f"A {szamlalo}/{nevezo} tört szám egész szám!  Értéke: {szamlalo/nevezo}")
else:
    print(f"A {szamlalo}/{nevezo} tört szám nem egész szám!")