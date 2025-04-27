def make_sandwich(*ingredients):
    print("\nPreparando un panino con i seguenti ingredienti:")
    for item in ingredients:
        print(f"- {item}")
    print("Il tuo panino è pronto!\n")

# Chiamate della funzione con un numero diverso di ingredienti
make_sandwich("prosciutto", "formaggio")
make_sandwich("pollo", "lattuga", "pomodoro", "maionese")
make_sandwich("tonno")