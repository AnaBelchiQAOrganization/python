# 1 Pedimos a la usuaria 5 veces que introduzca un color.

for i in range(5):
    color = input("Escribe un color: ")
    if color == "azul":
        print()
        print("¡Enhorabuena! Has sido premiada.")
        break
