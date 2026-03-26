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

#2) Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
# Pedir al usuario que cargue 5 productos
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)
# Mostrar la lista ordenada alfabéticamente
productos_ordenados = sorted(productos)
print("Lista de productos ordenada alfabéticamente:", productos_ordenados)
# Preguntar al usuario qué producto desea eliminar
producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("Producto eliminado. Lista actualizada:", productos)
else:
    print("El producto no se encuentra en la lista.")

    