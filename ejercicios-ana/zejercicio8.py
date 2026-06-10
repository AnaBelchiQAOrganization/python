# Escribir un programa que pida al usuario dos números enteros
# y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r>
# donde <n> y <m> son los números introducidos por el usuario,
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

def cociente(n, m):
    coc = n//m
    return coc


def resto(n, m):
    res = n % m
    return res


n = float(input("Escribe un número: "))
m = float(input("Escribe otro número: "))

print("El cociente de dividir el primer número entre el segundo es", cociente(n, m))
print("El resto de dividir el primer número entre el segundo es", resto(n, m))
