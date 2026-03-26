#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista.

import random

numeros = [random.randint(1, 100) for _ in range(15)]

# Mostrar los números generados
print("Números generados:")
for num in numeros:
    print(num, end=" ")
print()

# Crear una lista con los pares y otra con los impares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

# Mostrar los números pares
print("Números pares:")
for num in pares:
    print(num, end=" ")
print()

# Mostrar los números impares
print("Números impares:")
for num in impares:
    print(num, end=" ")
print()

# Mostrar cuántos números tiene cada lista
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))
