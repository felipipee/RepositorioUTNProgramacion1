diccionario_original = {
    'Argemtina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
}

diccionario_invertido = {valor: clave for clave, valor in diccionario_original.items()}

print(diccionario_original)
print(diccionario_invertido)