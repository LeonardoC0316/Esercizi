class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
marco = Person("Marco", 12)
chiara = Person("Chiara", 18)
flavio = Person("Flavio", 22)
print(alice.age)
if alice.age > bob.age:
    print(f"the oldest is {alice.age}")
else:
    print(f"the oldest is {bob.age}")

lista_di_persone = [alice, bob, marco, chiara, flavio]

p_min = lista_di_persone[0]
#giovane = lista_di_persone[0].name
for p in lista_di_persone:
    if p.age < p_min.age:
        p_min = p

print(f"il più giovane è: {p_min.name}")



