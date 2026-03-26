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
