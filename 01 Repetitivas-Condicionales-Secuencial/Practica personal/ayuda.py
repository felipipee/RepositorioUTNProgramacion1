#Hacemos el ejercicio del kiosco, con lista

nombre = ""
cant_productos = 0
precios = []
descuento_incluido = ""
precios_con_descuento = []


#Pedimos el nombre del cliente y verificamos que sean letras
nombre = input("Ingrese el nombre del cliente: ")
while nombre.isalpha() == False or nombre.strip() == "": #si no son letras o este vacío
    print("Error: El nombre debe contener solo letras.")
    nombre = input("Ingrese el nombre del cliente: ")
print(f"Hola {nombre}, bienvenido al kiosco de la facultad.")

cant_productos = input("Ingrese la cantidad de productos a comprar: ")
while cant_productos.isdigit() == False or int(cant_productos) <= 0: #si no es un número o es menor o igual a cero
    print("Error: La cantidad de productos debe ser un número entero mayor a cero.")
    cant_productos = input("Ingrese la cantidad de productos a comprar: ")

for i in range(int(cant_productos)):
    precio_producto = input(f"Ingrese el precio del producto {i+1}: ")
    while precio_producto.replace('.', '', 1).isdigit() == False or float(precio_producto) <= 0: #si no es un número o es menor o igual a cero
        print("Error: El precio del producto debe ser un número mayor a cero.")
        precio_producto = input(f"Ingrese el precio del producto {i+1}: ")
    precios.append(float(precio_producto))

    descuento_incluido = input(f"¿El producto {i+1} tiene descuento? (s/n): ").lower()
    while descuento_incluido not in ['s', 'n']: #si no es 's' o 'n'
        print("Error: Debe ingresar 's' para sí o 'n' para no.")
        descuento_incluido = input(f"¿El producto {i+1} tiene descuento? (s/n): ").lower()
    if descuento_incluido == 's':
        precio_con_descuento = float(precio_producto) * 0.9
        precios_con_descuento.append(precio_con_descuento)
    else:
        precios_con_descuento.append(float(precio_producto))



total_sin_descuento = sum(precios)
total_con_descuento = sum(precios_con_descuento)
ahorro_total = total_sin_descuento - total_con_descuento



print(f"Nombre del cliente: {nombre}")
print(f"Cantidad de productos comprados: {cant_productos}")
for i in range(int(cant_productos)):
    print(f"Precio del producto {i+1}: ${precios[i]:.2f}")
print(f"Valor final sin descuento: ${total_sin_descuento:.2f}")
print(f"Valor con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")


