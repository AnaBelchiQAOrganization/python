# 1 Pedimos a la usuaria un número entre 1 y 10

numero_elegido = int(input("Escribe un número del 1 al 10: "))

# 2 Definimos una función para comprobar si el número elegido es ganador o perdedor


def premiado(numero):
    if numero == 4:
        print("¡Enhorabuena, has acertado!")
    else:
        print("¡Lo sentimos. Has perdido!")
    return numero


# 3 Imprimimos el mensaje

mensaje = premiado(numero_elegido)

print(mensaje)
