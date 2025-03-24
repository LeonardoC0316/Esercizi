'''8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the  dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
Make at least one new function call that includes the number of songs on an album.'''


def make_album(artist_name, album_title, num_songs=None, **kwargs):
    # Crea il dizionario con il nome dell'artista e il titolo dell'album
    album_info = {
        'artist': artist_name,
        'title': album_title
    }
    
    # Se num_songs è stato fornito (non è None), aggiungilo al dizionario
    if num_songs is not None:
        album_info['num_songs'] = num_songs
    
    # Aggiungi gli altri parametri opzionali (come anno di uscita, ecc.) da kwargs
    for key, value in kwargs.items():
        album_info[key] = value
    
    return album_info

# Chiamate alla funzione per creare album
album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('Pink Floyd', 'The Dark Side of the Moon', num_songs=10)
album3 = make_album('Adele', '25', num_songs=11, year=2015)

# Stampa dei dizionari degli album
print(album1)
print(album2)
print(album3)
