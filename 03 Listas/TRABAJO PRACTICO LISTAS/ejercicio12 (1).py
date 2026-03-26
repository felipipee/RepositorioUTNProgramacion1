#12) Crear una lista vacía y pedir al usuario que ingrese 8 números enteros.
#• Mostrar la lista original.
#• Mostrar la lista ordenada de menor a mayor.
#• Mostrar la lista ordenada de mayor a menor.
#• Investigar el uso de sorted() y del parámetro reverse.

lista_numeros = []
for i in range(8):
    numero = int(input(f"Ingrese el número {i+1}: "))
    lista_numeros.append(numero)

# Mostrar la lista original
print("Lista original:")
for num in lista_numeros:
    print(num, end=" ")
print()

# Mostrar la lista ordenada de menor a mayor usando sorted()
lista_menor_a_mayor = sorted(lista_numeros)
print("Lista ordenada de menor a mayor:")
for num in lista_menor_a_mayor:
    print(num, end=" ")
print()

# Mostrar la lista ordenada de mayor a menor usando sorted() con reverse=True
lista_mayor_a_menor = sorted(lista_numeros, reverse=True)
print("Lista ordenada de mayor a menor:")
for num in lista_mayor_a_menor:
    print(num, end=" ")
print()
