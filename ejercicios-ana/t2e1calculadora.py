# 1 Pedimos dos números a la usuaria y los convertimos a número decimal

print("Voy a pedirte una serie de números para operar con ellos")

numero_1 = float(input("Escribe el primer número: "))
numero_2 = float(input("Escribe el segundo número: "))

# 1.1 Definimos las variables que almacenarán las operaciones

# 1.1.1 Suma de dos numeros
suma = numero_1 + numero_2

# 1.1.2 Resta de dos números
resta = numero_1 - numero_2

# 1.1.3 Multiplicación de dos números
multiplicacion = numero_1 * numero_2

# 1.1.4 división de dos números
division = numero_1 / numero_2

# 2 Mostramos el resultado mediante el comando print

print("El resultado de la suma es:", suma)
print("El resultado de la resta es:", resta)
print("El resultado de la multiplicación es:", multiplicacion)
print("El resultado de la división es:", division)
