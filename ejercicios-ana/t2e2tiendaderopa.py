# 1 Definimos los precios mediante variables

camiseta = 10
sudadera = 20.5
gorra = 5.5

# 2 Pedimos a la usuaria que introduzca la cantidad que quiere de cada artículo - Usamos input

cantidad_camiseta = int(input("¿Cuántas camisetas quieres? "))
cantidad_sudadera = int(input("¿Cuántas sudaderas quieres? "))
cantidad_gorra = int(input("¿Y gorras? "))

# 3 Calculamos el total de la compra usando operaciones básicas de suma y miltiplicación

precio_camisetas = camiseta * cantidad_camiseta
precio_sudaderas = sudadera * cantidad_sudadera
precio_gorras = gorra * cantidad_gorra

precio_sin_iva = precio_camisetas + precio_sudaderas + precio_gorras

print("Precio sin IVA=", precio_sin_iva, "€")

# 4 Añadimos el 21% de IVA

precio_con_iva = precio_sin_iva + (precio_sin_iva * 0.21)

# 5 Imprimimos el precio final

print("Total de la compra", precio_con_iva, "€")
