#13) Dada la siguiente lista de puntajes de un videojuego:
#puntajes = [450, 1200, 875, 990, 300, 1500, 640]
#• Mostrar el puntaje más alto y el más bajo.
#• Mostrar la lista ordenada de mayor a menor (ranking).
#• Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Mostrar el puntaje más alto y el más bajo
puntaje_mas_alto = max(puntajes)
puntaje_mas_bajo = min(puntajes)
print("El puntaje más alto es:", puntaje_mas_alto)
print("El puntaje más bajo es:", puntaje_mas_bajo)

# Mostrar la lista ordenada de mayor a menor (ranking)
ranking = sorted(puntajes, reverse=True)
print("Ranking (de mayor a menor):")
for i in range(len(ranking)):
    print(f"  Posición {i+1}: {ranking[i]}")

# Indicar en qué posición del ranking se encuentra el puntaje 990
posicion_990 = ranking.index(990) + 1  # +1 para que la posición arranque en 1
print("La posición del puntaje 990 en el ranking es:", posicion_990)
