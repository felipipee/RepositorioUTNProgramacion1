#4) Dada una lista con valores repetidos: 
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado.

valores_repetidos = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
# Crear una nueva lista sin elementos repetidos
valores_sin_repetidos = list(set(valores_repetidos))
# Mostrar el resultado
print("Lista original con valores repetidos:", valores_repetidos)
print("Lista sin valores repetidos:", valores_sin_repetidos)