voto = int(input("Inserire un voto: "))

'''while voto <1 or voto >10:
    print("voto non valido, il voto deve essere compreso tra 1 e 10")
    voto = int(input("Inserire un voto: "))'''

match voto:
    case 10:
        print("Eccellente")
    case 8|9:
        print("Molto buono")
    case 6|7:
        print("Sufficiente")
    case 4|5:
        print("Insufficiente")
    case 1|2|3:
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido!")
        
   

