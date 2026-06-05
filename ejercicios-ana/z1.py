# Dos formas de hacer el ejercicio t5e2
i = 0
while i < 5:
    color = input("Escribe un color: ")
    if color == "azul":
        print()
        print("¡Enhorabuena! Has sido premiada.")
        break
    i = i+1

# Añadimos más condiciones al while - comor rojo y longitud 8
i = 0
acertado = False
while i < 5 and acertado == False:
    color = input("Escribe un color: ")
    if color == "azul":
        acertado = True
        print()
        print("¡Enhorabuena! Has sido premiada.")
    elif color == "rojo":
        acertado = True
        print()
        print("Segundo premio")
    elif len(color) == 8:
        acertado = True
        print()
        print("Tercer premio")
    i = i+1
