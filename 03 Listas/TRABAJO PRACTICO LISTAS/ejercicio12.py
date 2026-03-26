#12) Crear una lista vacía y pedir al usuario que ingrese 8 números enteros. 
#• Mostrar la lista ordenada de menor a mayor.
#• Mostrar la lista ordenada de mayor a menor.
#• Investigue el uso de los métodos sort() y reverse().

lista_numeros = []
for i in range(8):
    numero = int(input(f"Ingrese el número {i+1}: "))
    lista_numeros.append(numero)
print("Lista de números ingresados:", lista_numeros)
lista_numeros.sort()
print("Lista de números ordenada:", lista_numeros)
lista_numeros.reverse()
print("Lista de números ordenada en orden inverso:", lista_numeros)