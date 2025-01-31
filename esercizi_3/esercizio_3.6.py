invitati = ["Elon", "Trump", "Obama"]

print("Ciao ragazzi ho trovato un tavolo più grande! Inviterò altre 3 persone.")

#aggiungiamo alla lista i nuovi invitati (i primi 2 all'inizio ed il terzo alla fine)
invitati.insert(0, "Tarantino")
invitati.insert(0, "Kim Yon Gun")
invitati.append("zin jin pin")

for invitato in invitati:
    print(f"Ciao {invitato}, sei stato così fortunato da essere stato invitato ad una cena cone me!")