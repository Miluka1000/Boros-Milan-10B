táv = float(input("Kérem adja meg a megjárt távot kilóméterben: "))
if táv <= 5:
    print("A futár díja 500ft.")
elif táv <= 10:
    print("A futár díja 1000ft.")
elif táv <= 15:
    print("A futár díja 1500ft.")
else:
    print("A futár díja 2000ft.")