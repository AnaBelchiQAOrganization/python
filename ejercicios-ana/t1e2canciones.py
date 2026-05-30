# 1. Pedimos a la usuaria que introduzca la información sobre su canción favorita

print("Introduce los datos que te pregunto a continuación sobre tu canción favorita")
print()

#1.1 Solicitamos el nombre de la canción
titulofav = input("¿Cual es tú canción favorita? ")
print()

#1.2 Solicitamos el autor
artistafav = input("¿Quién es el autor? ")
print()

#1.3 Solicitamos el album en el que aparece por primera vez
albumfav = input("¿En qué album fue publicada por primera vez? ")
print()

#1.4 Solicitamos el año de publicación y lo convertimos a entero
anyofav = int(input("¿Cuándo fue publicada por primera vez? "))
print()

#1.5 Solicitamos la duración en segundos de la canción y la convertimos a entero
duracionfav = int(input("¿Cuánto dura la canción? Dame la duración en segundos: "))
print()

#1.6 Preguntamos si la canción tiene videovideoclip
videoclipfav = input("¿La canción tiene videoclip? Reponde usando True o False: ")
print()

#2 Mostramos la información solicitada a la usuaria mediante el comando print

print("Ahora te voy a mostrar tus respuestas:")
print()
print("Tu canción favorita es",titulofav)
print("Es de",artistafav)
print("Apareció publicada por primera vez en el album",albumfav)
print("Que fue publicado en el año",anyofav)
print("La duración de la canción en segundos es",duracionfav)
print("¿La canción tiene videoclip?", videoclipfav)
print()

#3 Repetimmos el mismo ejercicio pero la canción más odiada

print("Introduce los datos que te pregunto a continuación sobre tu canción más odiada")
print()

#3.1 Solicitamos el nombre de la canción
titulohate = input("¿Cual es tú canción más odiada? ")
print()

#3.2 Solicitamos el autor
artistahate = input("¿Quién es el autor? ")
print()

#3.3 Solicitamos el album en el que aparece por primera vez
albumhate = input("¿En qué album fue publicada por primera vez? ")
print()

#3.4 Solicitamos el año de publicación y lo convertimos a entero
anyohate = int(input("¿Cuándo fue publicada por primera vez? "))
print()

#3.5 Solicitamos la duración en segundos de la canción y la convertimos a entero
duracionhate = int(input("¿Cuánto dura la canción? Dame la duración en segundos: "))
print()

#1.6 Preguntamos si la canción tiene videovideoclip
videocliphate = input("¿La canción tiene videoclip? Reponde usando True o False: ")
print()

#4 Mostramos la información solicitada a la usuaria mediante el comando print sobre su canción más odiada

print("Ahora te voy a mostrar tus respuestas sobre la canción que más odias")
print()
print("Tu canción más odiada es",titulohate)
print("Es de",artistahate)
print("Apareció publicada por primera vez en el album",albumhate)
print("Que fue publicado en el año",anyohate)
print("La duración de la canción en segundos es",duracionhate)
print("¿La canción tiene videoclip?", videocliphate)
print()