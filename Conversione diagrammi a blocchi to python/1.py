a = int(input("Inserire l'ipotenusa (a): "))
b = int(input("Insrire il cateto (b): "))
if a > b:
    c = ((a**2) - (b**2)) ** (1/2)
    print(f"Il cateto c: {c}")
else:
    print("Errore!")
