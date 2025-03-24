n = int(input("Inserire un numero: "))

while True:
    if n % 1 == 0 and n > 0:
        fattoriale = 1
        i = 1
        break
    else:
        print("il numero deve essere intero e positivo!")
        n = int(input("Inserire un numero"))
    

while i <= n:
    fattoriale *= i
    i += n
print(f"il fattoriale del numero è: {fattoriale}")


