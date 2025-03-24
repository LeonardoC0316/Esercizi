sum = 0
count = 0


while True:
    n = float(input("Inserire un numero: "))

    if n > 0:
        sum += n
    count += 1
    if count == 5:
        print(f"La somma è: {sum}")
        break