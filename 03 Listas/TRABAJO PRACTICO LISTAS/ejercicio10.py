#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 


ventas = [
    [10, 15, 20, 25, 30, 35, 40],  # Producto 1
    [5, 10, 15, 20, 25, 30, 35],   # Producto 2
    [8, 12, 16, 20, 24, 28, 32],   # Producto 3
    [7, 14, 21, 28, 35, 42, 49]    # Producto 4
]
# Mostrar el total vendido por cada producto
totales_productos = [sum(ventas[i]) for i in range(len(ventas))]

# Mostrar el día con mayores ventas totales
ventas_dias = [sum(ventas[i][j] for i in range(len(ventas))) for j in range(len(ventas[0]))]
dia_mayor_ventas = ventas_dias.index(max(ventas_dias)) + 1
# Indicar cuál fue el producto más vendido en la semana
producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print("Total vendido por cada producto:", totales_productos)
print("Día con mayores ventas totales:", dia_mayor_ventas)
print("Producto más vendido en la semana:", producto_mas_vendido)