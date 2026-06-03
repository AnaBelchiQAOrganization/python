# 1 Pedimos a la usuaria un número entre 1 y 10

numero_elegido = int(input("Escribe un número del 1 al 10: "))

# 2 Definimos una función para comprobar si el número elegido es ganador o perdedor


def premiado(numero):
    if numero == 4:
        mensaje = "¡Enhorabuena, has acertado!"
    else:
        mensaje = "¡Lo sentimos. Has perdido!"
    return mensaje


# 3 Imprimimos el mensaje

mensaje_usuaria = premiado(numero_elegido)

print()
print(mensaje_usuaria)
