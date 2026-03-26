#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista.

from operator import index
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