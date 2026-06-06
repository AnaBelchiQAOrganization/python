# 1 Creamos una lista con los 12 meses del año.

meses_del_anyo = ["Enero", "Febrero", "MArzo", "Abril", "Mayo", "Junio",
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# 2 Pedimos a la usuaria un número del 1 al 12.

numero = int(input("Escribe un número del 1 al 12: "))

# 3 Mostramos el mes correspondiente

print("El planeta que corresponde a ese mes del año es",
      meses_del_anyo[numero-1])

# 4 Si el mes es junio, muestra además el mensaje: EL MEJOR MES.

if numero == 6:
    print("¡EL MEJOR MES!")
