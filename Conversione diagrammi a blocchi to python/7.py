pari = 0
dispari = 0
count = 0
while count != 10:
    n = int((input("Inserire un numero: ")))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1
    count += 1
print(f"I numeri pari sono {pari}")
print(f"I numeri pari sono {dispari}")
