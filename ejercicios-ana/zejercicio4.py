# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

# Definimos la función genérica que nos resuelve la operación


def operacion_aritmetica(a, b, c):
    total = ((a+b)/(b*c))**b
    return total


# Solicitamos los valores a, b y c

a = float(input("Escribe un número: "))
b = float(input("Escribe otro número: "))
c = float(input("Escribe un tercero: "))

print("El resultado de la operación es", operacion_aritmetica(a, b, c))
