#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

notas = [
    [8, 7, 9],  # Estudiante 1
    [6, 8, 7],  # Estudiante 2
    [9, 9, 8],  # Estudiante 3
    [7, 6, 9],  # Estudiante 4
    [8, 7, 6]   # Estudiante 5
]

# Calcular el promedio de cada estudiante
promedios_estudiantes = []
for i in range(len(notas)):
    promedio = sum(notas[i]) / len(notas[i])
    promedios_estudiantes.append(promedio)

# Mostrar el promedio de cada estudiante
print("Promedios de los estudiantes:")
for i in range(len(promedios_estudiantes)):
    print(f"Estudiante {i+1}: {promedios_estudiantes[i]}")

# Calcular el promedio de cada materia
promedios_materias = []
for j in range(len(notas[0])):
    suma_materia = sum(notas[i][j] for i in range(len(notas)))
    promedio_materia = suma_materia / len(notas)
    promedios_materias.append(promedio_materia)

# Mostrar el promedio de cada materia
print("Promedios por materia:")
for j in range(len(promedios_materias)):
    print(f"Materia {j+1}: {promedios_materias[j]}")