# 1. Pedimos a la usuaria que introduzca la información sobre su canción favorita

print("Introduce los datos que te pregunto a continuación sobre tu canción favorita")
print()

# 1.1 Solicitamos el nombre de la canción
titulo_fav = input("¿Cual es tú canción favorita? ")
print()

# 1.2 Solicitamos el autor
artista_fav = input("¿Quién es el autor? ")
print()

# 1.3 Solicitamos el album en el que aparece por primera vez
album_fav = input("¿En qué album fue publicada por primera vez? ")
print()

# 1.4 Solicitamos el año de publicación y lo convertimos a entero
anyo_fav = int(input("¿Cuándo fue publicada por primera vez? "))
print()

# 1.5 Solicitamos la duración en segundos de la canción y la convertimos a entero
duracion_fav = int(
    input("¿Cuánto dura la canción? Dame la duración en segundos: "))
print()

# 1.6 Preguntamos si la canción tiene videovideoclip
videoclip_fav = input("¿La canción tiene videoclip? Reponde usando Sí/No: ")
print()

# 2 Mostramos la información solicitada a la usuaria mediante el comando print

print("Ahora te voy a mostrar tus respuestas:")
print()
print("Tu canción favorita es", titulo_fav)
print("Es de", artista_fav)
print("Apareció publicada por primera vez en el album", album_fav)
print("Que fue publicado en el año", anyo_fav)
print("La duración de la canción en segundos es", duracion_fav)
print("¿La canción tiene videoclip?", videoclip_fav)
print()

# 3 Repetimmos el mismo ejercicio pero la canción más odiada

print("Introduce los datos que te pregunto a continuación sobre tu canción más odiada")
print()

# 3.1 Solicitamos el nombre de la canción
titulo_odio = input("¿Cual es tú canción más odiada? ")
print()

# 3.2 Solicitamos el autor
artista_odio = input("¿Quién es el autor? ")
print()

# 3.3 Solicitamos el album en el que aparece por primera vez
album_odio = input("¿En qué album fue publicada por primera vez? ")
print()

# 3.4 Solicitamos el año de publicación y lo convertimos a entero
anyo_odio = int(input("¿Cuándo fue publicada por primera vez? "))
print()

# 3.5 Solicitamos la duración en segundos de la canción y la convertimos a entero
duracion_odio = int(
    input("¿Cuánto dura la canción? Dame la duración en segundos: "))
print()

# 1.6 Preguntamos si la canción tiene videovideoclip
videoclip_odio = input("¿La canción tiene videoclip? Reponde usando Sí/No: ")
print()

# 4 Mostramos la información solicitada a la usuaria mediante el comando print sobre su canción más odiada

print("Ahora te voy a mostrar tus respuestas sobre la canción que más odias")
print()
print("Tu canción más odiada es", titulo_odio)
print("Es de", artista_odio)
print("Apareció publicada por primera vez en el album", album_odio)
print("Que fue publicado en el año", anyo_odio)
print("La duración de la canción en segundos es", duracion_odio)
print("¿La canción tiene videoclip?", videoclip_odio)
print()
