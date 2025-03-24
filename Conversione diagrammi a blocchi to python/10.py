r = input("Inserire reddito: ")
m = input("Inserire media voti: ")
if r < 20000 and m > 27:
    print("Borsa di studio approvata!")
else:
    print("Borsa di studio rifiutata (reddito troppo alto o media troppo bassa)!")