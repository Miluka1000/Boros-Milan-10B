a = int(input("Adja meg a háromszög A oldalát: "))
b = int(input("Adja meg a háromszög B oldalát: "))
c = int(input("Adja meg a háromszög C oldalát: "))

if a + b > c and b + c > a and a + c > b:
    print("A háromszög megrajzolható.")
else:
    print("A háromszög nem rajzolható meg.")