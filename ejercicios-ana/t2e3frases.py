# 1 Pedimos a la usuaria que introduzca una frase mediante input

frase = input("Escribe una frase: ")

# 2 Mostramos los resultados de las operaciones con cadenas mediante print

# 2.1 Calculamos la longitud de la frase mediante len y la imprimimos

longitud = len(frase)
print("Tu frase tiene", longitud, "caracteres incluidos los espacios")

# 2.2 Escribimos la frase en mayúsculas mediante upper y la imprimimos

mayusculas = frase.upper()
print("Esta es la frase escrita en mayúsculas:", mayusculas)

# 2.2 Escribimos la frase en minúsculas mediante lower y la imprimimos

minusculas = frase.lower()
print("Esta es la frase escrita en minúsculas:", minusculas)
