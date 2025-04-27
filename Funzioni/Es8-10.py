lista = ["Ciao", "Buongiorno", "Arrivederci", "Grazie"]

def show_messages(a):
    for e in a:
        print(e)

show_messages(lista)

sent_messages = []

def send_messages(a):
    for e in a:
        print(e)
        sent_messages.append(e)

send_messages(lista)

print(lista)
print(sent_messages)

