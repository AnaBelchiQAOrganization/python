# Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

productos = input("Escribe el nombre de los productos separados por comas: ")

print("La lista en diferentes líneas es: " +
      "\n" + productos.replace(", ", "\n"))
