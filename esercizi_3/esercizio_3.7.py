invitati = ["Elon", "Trump", "Obama"]

print("Ciao ragazzi ho trovato un tavolo più grande! Inviterò altre 3 persone.")

#aggiungiamo alla lista i nuovi invitati (i primi 2 all'inizio ed il terzo alla fine)
invitati.insert(0, "Tarantino")
invitati.insert(0, "Kim Yon Gun")
invitati.append("zin jin pin")

for invitato in invitati:
    print(f"Ciao {invitato}, sei stato così fortunato da essere stato invitato ad una cena cone me!")


print("Ciao ragazzi, purtroppo sono rimasti solo 2 posti disponibli per lanciare i missili nucleari sta sera a tavola con me")

while len(invitati) > 2:

    print(f"{invitati[0]} Mi dispiace ma non hai abbastanza missili nucleari :c")
    invitati.pop(0)

for invitato in invitati:
    print("Complimenti! Hai abbastanza missili nucleari e debito pubblico per cenare con me.")

del invitati[:]

print(invitati)