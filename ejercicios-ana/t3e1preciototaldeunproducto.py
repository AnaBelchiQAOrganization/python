# 1 Solicitamos los datos del producto que va a comprar

print("Rellena los datos que te pido a continuación:")

nombre_producto = input("Nombre del producto: ")

precio_unidad = float(input("¿Cuánto cuesta? "))

cantidad = int(input("¿Cuántas unidades vas a comprar? "))

descuento = float(input("¿Qué porcentaje de descuento tiene? "))

iva = int(input("¿Cuál es el porcentaje de IVA aplicado? "))

# 2 Definimos la función


def calcular_total(precio_unidad, cantidad, descuento, iva):
    coste_producto = precio_unidad * cantidad
    total_descuento = (descuento / 100) * coste_producto
    subtotal = coste_producto - total_descuento
    coste_iva = (iva / 100) * subtotal
    total = subtotal + coste_iva
    return total


# 2.1 Usamos la función para calcular el total con los datos pedidos a la usuaria

total_compra = calcular_total(precio_unidad, cantidad, descuento, iva)

# 3 Imprimimos el total de la compra

print("El valor de tu compra es de ", total_compra, "€")
