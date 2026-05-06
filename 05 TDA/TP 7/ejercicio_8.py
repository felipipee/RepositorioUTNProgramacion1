productos = {
    "manzana": 4,
    "banana": 7,
    "naranja": 20,
    "leche": 10,
    "pan": 5,
    "galletas": 15
}


consulta = input("Ingrese el nombre del producto que desea consultar: ").lower()
while not consulta.isalpha():
    print("Error, ingrese solo texto")
    consulta = input("Ingrese el nombre del producto que desea consultar: ").lower()

if consulta in productos:
    print(f"El stock de {consulta} es: {productos[consulta]}")

    agregar_stock = input("¿Desea agregar stock? (S/N): ").upper()
    while agregar_stock != "S" and agregar_stock != "N":
        print("Error, ingrese solo S o N")
        agregar_stock = input("¿Desea agregar stock? (S/N): ").upper()

    if agregar_stock == "S":
        cantidad_agregar = input("Ingrese la cantidad a agregar: ")
        while not cantidad_agregar.isdigit():
            print("Error, ingrese solo números")
            cantidad_agregar = input("Ingrese la cantidad a agregar: ")
        cantidad_agregar = int(cantidad_agregar)
        productos[consulta] += cantidad_agregar
        print(f"Nuevo stock de {consulta}: {productos[consulta]}")

    else:
        print("No se ha agregado stock.")

else:
    print("Producto no encontrado en el inventario.")
    nuevo_producto = input("¿Desea agregar este producto al inventario? (S/N): ").upper()
    while nuevo_producto != "S" and nuevo_producto != "N":
        print("Error, ingrese solo S o N")
        nuevo_producto = input("¿Desea agregar este producto al inventario? (S/N): ").upper()
    if nuevo_producto == "S":
        cantidad_nuevo = input("Ingrese la cantidad del nuevo producto: ")
        while not cantidad_nuevo.isdigit():
            print("Error, ingrese solo números")
            cantidad_nuevo = input("Ingrese la cantidad del nuevo producto: ")
        cantidad_nuevo = int(cantidad_nuevo)
        productos[consulta] = cantidad_nuevo
        print(f"Producto {consulta} agregado con stock de {cantidad_nuevo}.")
    else:
        print("No se ha agregado el producto al inventario.")
