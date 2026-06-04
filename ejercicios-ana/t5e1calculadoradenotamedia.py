# 1 Definimos la función recogida de notas

def calcular_nota_media(cuantas):
    suma = 0

    for i in range(cuantas):
        nota = float(input("Dame las notas: "))
        suma = suma+nota

    # Calculamos la media

    media = suma/cuantas
    return media


# 2 Pedimos a la usuaria cuantas notas quiere introducir

cuantas_notas = int(input("¿Cuántas notas quieres introducir?"))

# 4 Imprimimos la media

print("Tu nota media es", calcular_nota_media(cuantas_notas))
