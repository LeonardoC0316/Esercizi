'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are
large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message,
and a shirt of any size with a different message.'''

def make_shirt(d_size = "L", d_text = "I love Python"):
    print(f"The size of the shirt is {d_size} and the text on it is {d_text}")
make_shirt("M", "Ciaoo!")
