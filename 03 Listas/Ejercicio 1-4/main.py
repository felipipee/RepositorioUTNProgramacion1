Lista_Productos = []
Stock_Productos = []
Precios_Productos = []

while True:
    print("_" * 40)
    print("\nElija una opción")
    print("1.Alta individual - Ingreso de 1 producto")
    print("2.Carga Masiva - Ingreso de varios productos")
    print("3.Baja de Producto: Eliminar un producto por su nombre")
    print("4.Consultas Rápidas: Buscar un producto por nombre y elegir si ver su Stock o su Precio")
    print("5.Movimiento de Stock")
    print("6.Alerta de Agotados")
    print("7.Listado General")
    print("8.Salir del Programa")
    opcion = input("Ingrese la opción ")
    match opcion:
        case "1":
            print("")
            print("")
            print("Carga de Producto")
            nombre_producto = input("Ingrese el nombre del producto: ").strip().capitalize()
            while nombre_producto == "" or nombre_producto.isdigit():
                print("Nombre inválido, asegurese de ingresar el nombre")
                nombre_producto = input("Ingrese el nombre del producto: ").strip().capitalize()
            else:
                print(f"Producto guardado como {nombre_producto}")
                Lista_Productos.append(nombre_producto)
            precio = input("Ingrese el precio para el producto $").strip
            while precio == "":
                print("Precio inválido, asegurese de ingresar el precio")
                precio = input("Ingrese el precio del producto: ")
            while (precio).isalpha():
                print("Precio inválido, asegurese de ingresar el precio")
                precio = input("Ingrese el precio del producto: ")
            else:
                float(precio)
                print(f"precio del producto = {precio}")
                Precios_Productos.append(precio)
            stock = input("Ingrese el stock del producto")
            while (stock).isalpha():
                print("Cantidad inválida, asegurese de ingresar el stock correcto")
                stock = input("Ingrese el stock del producto: ")
            else:
                float(stock)
                print(f"Stock del producto = {stock}")
                Stock_Productos.append(stock)
            print(Lista_Productos, Precios_Productos, Stock_Productos)
            


        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            break
        case _:
            print("Ingrese una opcion de la lista")