'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''
def check_lenght(str:str):
    if len(str) > 10:
        print("la stringa è maggiore di 10 caratteri")
    elif len(str) < 10:
        print("la stringa è minore di 10 caratteri")
    else:
        print("la stringa è di 10 caratteri")

check_lenght("ciao")