precios_totales = []
total = 0
total_sin_descuento = 0
total_venta = 0

ventas_realizadas = 0



vendedor = input("Ingrese el nombre del vendedor encargado: ").capitalize()
while not vendedor.isalpha():
        print("Opción inválida")
        vendedor = input("Ingrese el nombre del vendedor encargado: ").capitalize()
print(f"Bienvenido/a {vendedor}")

while True:
    print("Elija la acción que desea procesar")
    print("1. Hacer ventas")
    print("2. Finalizar el día y mostrar resumen final")
    accion = input("Ingrese la acción a procesar")
    match accion:
        case'1':
            venta = input("Hacer otra venta? (s/n): ")
            while venta != 's' and venta != 'n':
                print("Opción inválida")
                venta = input("Hacer otra venta? (s/n): ")
            if venta == 's':
                nombre_cliente = input("¿Cuál es el nombre del cliente?: ")
                while not nombre_cliente .isalpha():
                    print("Opción inválida")
                    nombre_cliente = input("Ingrese el nombre del cliente: ").capitalize()
                productos_a_comprar = input("Cuantos productos desea vender? (número): ")
                while not productos_a_comprar.isdigit:
                    print("Opción inválida, ingrese un número: ")
                    productos_a_comprar = input("Cuántos productos desea vender?: ")
                for i in range(int(productos_a_comprar)):
                    precio = input("Cuál es el precio del producto?: ")
                    while not precio.isdigit:
                        print("Opción inválida, ingrese un número: ")
                        precio = input("Cuál es el precio del producto?: ")
                    precio = float(precio)
                    total_sin_descuento = total_sin_descuento + int(precio)
                    descuento = input("Tiene descuento?: ")
                    while not descuento != 's' and venta != 'n':
                        print("Opción inválida")
                        descuento = input("Tiene descuento?: ")
                    if descuento == 'y':
                        total = total + int(precio) * 0.85
                        total_venta = total_venta + precio * 0.85
                        print("Precio con descuento ingresado")
                    elif descuento == 'n':
                        total = total + int(precio)
                        total_venta = total_venta + precio
                        print("Precio ingresado")
                ahorro = total_sin_descuento - total_venta
                ventas_realizadas =+ 1
                precios_totales.append(total_venta)
                print("Venta realizada, precio total sin descuento: ")
                print(f"\n {total_sin_descuento}")
                print("Precio total con descuentos incluidos ")
                print(F"\n {total_venta}")
                print("Ahorro total")
                print(F"\n {ahorro}")
            else: 
                pass
        case '2':
            maximo = (max(precios_totales))
            promedio = (sum(precios_totales) / len(precios_totales))
            print("Finalizando el día.")
            print("Ventas realizadas ")
            print(f"\n {ventas_realizadas}")
            print("Dinero ingresado en el turno ")
            print(f"\n {total}")
            print("Precios por venta en el turno ")
            print(f"\n {precios_totales}")
            print("Mayor venta del día")
            print(f"\n {maximo}")
            print("Promedio ")
            print(f"\n {promedio}")
            
        case _:
            print("Opción no valida, ingrese una opción de la lista")