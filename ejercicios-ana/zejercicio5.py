# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = float(input("¿Cuántas horas has trabajado este més?: "))
coste_hora = float(input("¿Cuánto te pagan por hora?: "))

salario_mes = horas_trabajadas*coste_hora

print("Este mes vas a cobrar", salario_mes, "€")
