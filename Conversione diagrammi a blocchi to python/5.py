n = int(input("Inserire un numero: "))

primo = True

if n < 2:
    primo = False
else:
    div = 2
    if div < n:
        if n % div == 0:
    
            primo = True
        else:
            div += 1
    else:
        primo = False

if primo == True:
    print("Il numero primo!")
else:
    print("Il numero non è primo!")
