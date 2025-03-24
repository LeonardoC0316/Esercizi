# dal file peronsa.py importa la classe Persona 
'''from persona import Persona

# creare un oggetto di tipo persona
lc:Persona = Persona("Leonardo", "Cimitan", 21)

print(lc)

print(lc.name, lc.lastname, lc.age)
'''

# dal file persona2.py importa la classe Persona
from persona2 import Persona

lc:Persona = Persona()

# voglio richiamare la funzione displayData della classe Persona per stampare in output le informazioni relative alla persona lc
lc.displayData() 

# impostare il nome della persona lc
lc.setName("Leonardo")

print("-----")
lc.displayData()

# impostare il cognome della persona lc

lc.setLastname("Cimitan")

#impostare l'età della persona lc
lc.setAge(-21)

print("-----")
lc.displayData()
