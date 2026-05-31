# 1 Pedimos a la usuaria que escriba su correo electrónico

correo = input("Escribe tu correo electrónico: ")

# 2 Mostramos los resultados de las operaciones con cadenas mediante print

# 2.1 Calculamos la longitud del correo mediante len y la imprimimos

longitud_correo = len(correo)

print("La longitud de tu correo electrónico es de",
      longitud_correo, "caracteres")

# 2.2 Escribimos el correo en mayúsculas mediante upper y lo imprimimos

correo_mayusculas = correo.upper()
print("Tu correo electrónico escrito en mayúsculas se ve así:", correo_mayusculas)

# 2.3 Escribimos el correo en minúsculas mediante lower y lo imprimimos

correo_minusculas = correo.lower()
print("Este es tu correo electrónico escrito en minúsculas:", correo_minusculas)
