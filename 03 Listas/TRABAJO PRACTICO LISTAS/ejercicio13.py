#13) Dada una lista con los puntajes de juegos, encontrar el puntaje más alto, el más bajo y la posición del puntaje 990.



puntajes = [450, 1200, 875, 990, 300, 1500, 640]
puntaje_mas_alto = max(puntajes)
print("El puntaje más alto es:", puntaje_mas_alto)
puntaje_mas_bajo = min(puntajes)
print("El puntaje más bajo es:", puntaje_mas_bajo)
posicion_990 = puntajes.index(3)
print("La posición del puntaje 990 es:", posicion_990)