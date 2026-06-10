# Escribir un programa que lea un entero positivo, n,
# introducido por el usuario y después muestre en pantalla
# la suma de todos los enteros desde 1 hasta n.

def suma_serie(n):
    suma = (n*(n+1))/2
    return suma

# Pedimos al usuario el número


n = int(input("Escribe un número entero. Vamos a calcular la suma de los enteros que hay entre 1 y tu número: "))

print("La suma de los enteros entre 1 y tu número es", int(suma_serie(n)))
