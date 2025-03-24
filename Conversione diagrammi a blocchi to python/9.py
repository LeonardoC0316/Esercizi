nome = input("Inserire il nome: ")
vendite = input("Vendite: ")

max_nome = nome
massimo = vendite
min_nome = nome
minimo = vendite
count = 1



while count < 20:
    new_nome = input("Inserisci un altro nome: ")
    new_vendite = input("Inserire nuove vendite: ")
    if new_vendite > massimo:
        max_nome = new_nome
        massimo = new_vendite
    else:
        if new_vendite < minimo:
            min_nome = new_nome
            minimo = new_nome
    count += 1

print(max_nome, massimo)
print(min_nome, minimo)



    
