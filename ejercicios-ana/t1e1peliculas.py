# 1. Declaramos variables para guardar la información de mi peli favorita

titulo = "Cinema paradiso"

director = "Giuseppe Tornatore"

anyo = 1988

genero = "Drama"

duracion = 124

premios = True

# 2. Imprimimos la info de mi peli favorita

print("Mi película favorita es", titulo)
print("La dirigió", director)
print("Se estrenó el año", anyo)
print("Pertenece al género", genero)
print("Dura", duracion, "m")
print("¿Ganó algún premio?", premios)
print()

# 2.1 - Imprimimos en tipo párrafo

print("Mi película favorita es", titulo, ", dirigida por", director,
      ". Se estrenó el año", anyo, ", perteneciendo al género", genero,
      ", con una duración de", duracion, "minutos.")
print("¿Ganó algún premio?", premios)
print()

# 3. Traducimos los valores de las variables a inglés

titulo = "Cinema paradiso (EN)"

director = "Giuseppe Tornatore (EN)"

genero = "Drama (EN)"

# anyo,duracion y premio - Al ser el mismo valor que el declarado anteriormente, no es necesario volver a escribirla

# 4. Volvemos a imprimir la info de mi peli favorita

print("Mi película favorita es", titulo)
print("La dirigió", director)
print("Se estrenó el año", anyo)
print("Pertenece al género", genero)
print("Dura", duracion, "m")
print("¿Ganó algún premio?", premios)
print()
