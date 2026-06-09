# 1 Pedimos a la usuaria que introduzca una cantidad en euros

cantidad_euros = float(input("Escribe una cantidad cualquiera en euros: "))

# 2 Convertimos las cantidades a dólares ya libras mediante dos funciones


def cambiar_moneda(euros):
    a_dolar = (euros/1.1)
    a_libra = (euros/0.87)
    return a_dolar, a_libra


# 3 Mostramos los resultados mediante print y una llamada a la función cambiar_moneda

cambio_dolar, cambio_libra = cambiar_moneda(cantidad_euros)

print("El cambio en dólares es de ", round(cambio_dolar, 2), "$")
print("El cambio en libras es de ", round(cambio_libra, 2), "£")
