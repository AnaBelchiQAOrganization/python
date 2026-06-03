# 1 Pedimos a la usuaria que elija un color

color = input(
    "Elije uno de estos colores: rojo, verde, azul, amarillo o morado: ")

# 2 Definimos la función mensaje_color para seleccionar el mensaje según el color elegido


def mensaje_color(color_func):
    if color_func == "rojo":
        print("Tu mensaje es un mensaje de pasión y energía.")
    elif color_func == "verde":
        print("Tu mensaje es un mensaje de esperanza y crecimiento.")
    elif color_func == "azul":
        print("Tu mensaje es un mensaje de calma y serenidad.")
    elif color_func == "amarillo":
        print("Tu mensaje es un mensaje de felicidad y optimismo.")
    else:
        print("Tu mensaje es un mensaje de sabiduría y creatividad.")
    return color_func


# 3 Mostramos un mensaje concreto en función del color elegido

mensaje = mensaje_color(color)

print(mensaje)
