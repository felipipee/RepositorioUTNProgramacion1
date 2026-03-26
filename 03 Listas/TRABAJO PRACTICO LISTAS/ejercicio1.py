
#1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja.

notas = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
# Mostrar la lista completa
print("Lista de notas:", notas)
# Calcular y mostrar el promedio
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)
# Indicar la nota más alta y la más baja
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print("Nota más alta:", nota_mas_alta)
print("Nota más baja:", nota_mas_baja)