valor_final = 0.0
valor_con_descuento = 0.0
ahorro = 0.0

print("*" * 30)
print("Bienvenido al kiosco de la facultad")
print("*" * 30)

nombre = input("Ingrese el nombre del cliente: ")  #pedimos nombre y verificamos que sean letras
while nombre.isalpha() == False: #si no son letras
    print("Error: El nombre debe contener solo letras.")
    nombre = input("Ingrese el nombre del cliente: ")
while len(nombre)<1:  #si esta vacio
    print("Error: El nombre no puede estar vacío.")
    nombre = input("Ingrese el nombre del cliente: ")

print("*" * 30)

productos_a_comprar = int(input("Ingrese la cantidad de productos a comprar: "))
while productos_a_comprar <= 0: #si es menor o igual a cero, vacio
    print("Error: La cantidad de productos debe ser mayor a cero.")
    productos_a_comprar = int(input("Ingrese la cantidad de productos a comprar: "))
while not isinstance(productos_a_comprar, int):
    print("Error: La cantidad de productos debe ser un número entero.")
    productos_a_comprar = int(input("Ingrese la cantidad de productos a comprar: "))

print("*" * 30)

for i in range(productos_a_comprar):
    precio_producto = float(input(f"Ingrese el precio del producto {i+1}: "))
    while precio_producto <= 0:
        print("Error: El precio del producto debe ser mayor a cero.")
        precio_producto = float(input(f"Ingrese el precio del producto {i+1}: "))
    valor_final += precio_producto
    descuento_incluido = input(f"¿El producto {i+1} tiene descuento? (s/n): ").lower()
    while descuento_incluido not in ['s', 'n']:
        print("Error: Debe ingresar 's' para sí o 'n' para no.")
        descuento_incluido = input(f"¿El producto {i+1} tiene descuento? (s/n): ").lower()
    if descuento_incluido == 's':
        precio_producto = precio_producto * 0.9
        valor_con_descuento += precio_producto
    else:
        break

print(f"Nombre del cliente: {nombre}")
print(f"Cantidad de productos comprados: {productos_a_comprar}")
for i in range(productos_a_comprar):
    print(f"2Precio del producto {i+1}: ${precio_producto:.2f}")
print(f"Valor final sin descuento: ${valor_final:.2f}")
print(f"Valor con descuento: ${valor_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")