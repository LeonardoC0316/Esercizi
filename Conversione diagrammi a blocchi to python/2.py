# usando il ciclo while
max = float(input("Inserire il primo numero: "))
i = 1

while i < 4:
    i += 1
    n = float(input("Inserire un numero: "))
    if n > max:
        max = n

print(f"Il massimo tra i 4 numeri inseriti è: {max}")

# usando il ciclo for 

'''max = float(input("Inserire il primo numero: "))
i = 0

for i in range(3):
    i += 1
    n = float(input("Inserire un numero: "))
    if n > max:
        max = n

print(f"Il massimo tra i 4 numeri inseriti è: {max}")'''