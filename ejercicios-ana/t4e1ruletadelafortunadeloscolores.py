# 1 Pedimos a la usuaria que elija un color

color = input(
    "Elije uno de estos colores: rojo, verde, azul, amarillo o morado: ")

# 2 Definimos la función mensaje_color para seleccionar el mensaje según el color elegido


def mensaje_color(color_func):
    if color_func == "rojo":
        mensaje = "pasión y energía."
    elif color_func == "verde":
        mensaje = "esperanza y crecimiento."
    elif color_func == "azul":
        mensaje = "calma y serenidad."
    elif color_func == "amarillo":
        mensaje = "felicidad y optimismo."
    else:
        mensaje = "sabiduría y creatividad."
    return mensaje


# 3 Mostramos un mensaje concreto en función del color elegido

mensaje_mostrado = mensaje_color(color)

print("Tu mensaje es un mensaje de", mensaje_mostrado)
