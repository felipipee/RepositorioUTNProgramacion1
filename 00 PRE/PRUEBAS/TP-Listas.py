#1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja.

notas = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
# Mostrar la lista completa
print("Lista de notas:", notas)
# Calcular y mostrar el promedio
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)
# Indicar la nota más alta y la más baja
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print("Nota más alta:", nota_mas_alta)
print("Nota más baja:", nota_mas_baja)


#2) Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
# Pedir al usuario que cargue 5 productos
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)

# Mostrar la lista ordenada alfabéticamente
productos_ordenados = sorted(productos)
print("Lista de productos ordenada alfabéticamente:", productos_ordenados)

# Preguntar al usuario qué producto desea eliminar
producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("Producto eliminado. Lista actualizada:", productos)
else:
    print("El producto no se encuentra en la lista.")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista.

import random
numeros = [random.randint(1, 100) for _ in range(15)]
# Crear una lista con los pares y otra con los impares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
# Mostrar cuántos números tiene cada lista
print("Números generados:", numeros)
print("Números pares:", pares)
print("Números impares:", impares)

print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))


#4) Dada una lista con valores repetidos: 
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado.

valores_repetidos = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
# Crear una nueva lista sin elementos repetidos
valores_sin_repetidos = list(set(valores_repetidos))
# Mostrar el resultado
print("Lista original con valores repetidos:", valores_repetidos)
print("Lista sin valores repetidos:", valores_sin_repetidos)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada.

estudiantes = ["Ana", "Luis", "Marta", "Carlos", "Sofía", "Jorge", "Lucía", "Pedro"]
print("Lista de estudiantes:", estudiantes)
# Preguntar al usuario si quiere agregar o eliminar un estudiante
accion = input("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)? ").upper()
if accion == 'A':
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado.")
elif accion == 'E':
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print("Estudiante eliminado.")
    else:
        print("El estudiante no se encuentra en la lista.")
# Mostrar la lista final actualizada
print("Lista final de estudiantes:", estudiantes)



#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero). 

numeros = [10, 20, 30, 40, 50, 60, 70]
# Rotar los elementos una posición hacia la derecha
ultimo_numero = numeros.pop()  # Eliminar el último elemento
numeros.insert(0, ultimo_numero)  # Insertarlo al inicio
# Mostrar la lista rotada
print("Lista rotada hacia la derecha:", numeros)

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





#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada. 


# Inicializar el tablero de Ta-Te-Ti
tablero = [["-" for _ in range(3)] for _ in range(3)]

# Mostrar el tablero inicial
print("Tablero inicial:")
for fila in tablero:
    print(" ".join(fila))

# Permitir que dos jugadores ingresen posiciones para colocar "X" o "O"
jugador_actual = "X"
for turno in range(9):
    print(f"Turno del jugador {jugador_actual}")
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador_actual
        print("Tablero actualizado:")
        for fila_tablero in tablero:
            print(" ".join(fila_tablero))
        
        # Cambiar de jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"
    else:
        print("Casilla ocupada. Intente otra.")






#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 


ventas = [
    [10, 15, 20, 25, 30, 35, 40],  # Producto 1
    [5, 10, 15, 20, 25, 30, 35],   # Producto 2
    [8, 12, 16, 20, 24, 28, 32],   # Producto 3
    [7, 14, 21, 28, 35, 42, 49]    # Producto 4
]
# Mostrar el total vendido por cada producto
totales_productos = [sum(ventas[i]) for i in range(len(ventas))]

# Mostrar el día con mayores ventas totales
ventas_dias = [sum(ventas[i][j] for i in range(len(ventas))) for j in range(len(ventas[0]))]
dia_mayor_ventas = ventas_dias.index(max(ventas_dias)) + 1
# Indicar cuál fue el producto más vendido en la semana
producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print("Total vendido por cada producto:", totales_productos)
print("Día con mayores ventas totales:", dia_mayor_ventas)
print("Producto más vendido en la semana:", producto_mas_vendido)

