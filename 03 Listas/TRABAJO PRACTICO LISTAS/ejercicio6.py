#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero). 

numeros = [10, 20, 30, 40, 50, 60, 70]
# Rotar los elementos una posición hacia la derecha
ultimo_numero = numeros.pop()  # Eliminar el último elemento
numeros.insert(0, ultimo_numero)  # Insertarlo al inicio
# Mostrar la lista rotada
print("Lista rotada hacia la derecha:", numeros)