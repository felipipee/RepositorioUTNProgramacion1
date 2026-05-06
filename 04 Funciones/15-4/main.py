from fcs import *

notas = []
print("Ingrese las notas de los alumnos (ingrese -1 para finalizar):")
while True:
    try:
        nota = float(input("Nota: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    if nota > 10:
        print("La nota no puede ser mayor a 10.")
        continue
    if nota == -1:
        break
    notas.append(nota)
print(notas)
calcular_promedio(notas)


notas_segundo = []
print("Ingrese las notas de los alumnos del segundo año (ingrese -1 para finalizar):")
while True:
    try:
        nota = float(input("Nota: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    if nota > 10:
        print("La nota no puede ser mayor a 10.")
        continue
    if nota == -1:
        break
    notas_segundo.append(nota)
print(notas_segundo)
calcular_promedio(notas_segundo)
aprobados(notas_segundo)

notas_tercero = []
print("Ingrese las notas de los alumnos del tercer año (ingrese -1 para finalizar):")
while True:
    try:
        nota = float(input("Nota: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    if nota > 10:
        print("La nota no puede ser mayor a 10.")
        continue
    if nota == -1:
        break
    notas_tercero.append(nota)
print(notas_tercero)
analizar_notas(notas_tercero)