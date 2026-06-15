# 1 Creamos una lista con los 8 planetas del sistema solar

planetas_sistema_solar = ["Mercurio", "Venus", "La Tierra",
                          "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

# 2 Pedimos a la usuaria un número: ¿el enunciado es erróneo?
# Vamos a pedir un número para poder dar un resultado malo,
# sin especificar el rango en el que está.

numero = int(input("Escribe un número: "))

# 3 Mostramos el planeta correspondiente. La variable numero será el indice de la lista.
# Ojo: el indice empieza en 0 no en 1
# Si el número es inválido mostraremos un mensaje de error

if numero in range(1, 8):
    print("El planeta que has elegido es", planetas_sistema_solar[numero-1])
else:
    print("Error: No es un número válido")
