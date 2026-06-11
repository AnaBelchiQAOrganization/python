# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contrasenya = "SuperSegura"

contrasenya_usuario = input("¿Cuál es tu contraseña? ")

if contrasenya.lower() == contrasenya_usuario.lower():
    print("Tu contraseña coincide con la que está guardada")
else:
    print("tu contraseña no es la correcta")
