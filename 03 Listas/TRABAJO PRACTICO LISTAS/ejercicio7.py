#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [15, 25],  # Día 1
    [17, 27],  # Día 2
    [14, 22],  # Día 3
    [16, 26],  # Día 4
    [18, 28],  # Día 5
    [13, 23],  # Día 6
    [19, 29]   # Día 7
]

# Calcular el promedio de las mínimas y el de las máximas
minimas = [temp[0] for temp in temperaturas]
maximas = [temp[1] for temp in temperaturas]
promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)

# Mostrar en qué día se registró la mayor amplitud térmica
amplitudes = [maxima - minima for minima, maxima in temperaturas]
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1
print("Día con mayor amplitud térmica:", dia_mayor_amplitud)