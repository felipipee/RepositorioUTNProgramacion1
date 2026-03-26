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