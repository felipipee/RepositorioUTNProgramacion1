clientes_unicos = set() # set
gastos_por_cliente = {} # diccionario
ventas = []

def cargar_ventas():

    while True:
        cliente = input("Ingrese nombre del cliente (o 'fin' para terminar): ")

        if cliente.lower() == "fin":

            break

        productos = input("Ingrese productos separados por coma: ").split(",")
        productos = [p.strip() for p in productos]
    
        total = float(input("Ingrese total de la compra: "))
    
        venta = (cliente, productos, total) # tupla
        ventas.append(venta) # lista
        return ventas
    
def procesar_ventas(ventas):
    for cliente, productos, total in ventas:
        clientes_unicos.add(cliente)
    if cliente in gastos_por_cliente:
        gastos_por_cliente[cliente] += total
    else:
        gastos_por_cliente[cliente] = total
    return clientes_unicos, gastos_por_cliente

def mostrar_resumen(ventas, clientes_unicos, gastos):
    print("\nClientes únicos:")
    print(clientes_unicos)
    print("\nGastos por cliente:")
    for cliente, total in gastos.items():
        print(cliente, "->", total)
    # cliente que más gastó
    max_cliente = max(gastos, key=gastos.get)
    print("\nCliente que más gastó:", max_cliente)
    print("\nVentas mayores a 5000:")
    for venta in ventas:
        if venta[2] > 5000: # condicional
            print(venta)


while True:
    print("\n ------------Menú------------")
    print("\nOpción 1: Cargar Ventas")
    print("\nOpción 2: Ver clientes únicos y gastos por cliente")
    print("\nOpción 3: Mostrar resumen de ventas")
    print("\nOpción 4: ")
    print("\nOpción 5: opcion5")
    print("\nOpción 6: opcion6")
    print("\nOpción 7: opcion7")
    print("\nOpción 8: Salir")
    print("\n --------Fin del menú--------")

    opcion = input("Ingrese la opción que desee procesar ")
    while not opcion.isdigit():
        print("Error, ingrese solo numeros")
        opcion = input("Ingrese la opción que desee procesar ")
    opcion = int(opcion)

    match opcion:
        case 1:
            ventas = cargar_ventas()
            if len(ventas) > 0: # condicional
                clientes, gastos = procesar_ventas(ventas)
                mostrar_resumen(ventas, clientes, gastos)
            else:
                print("No se ingresaron ventas")


            procesar_ventas(ventas)

            pass
        case 2:
            pass
        case 3:
            mostrar_resumen(ventas, clientes_unicos, gastos_por_cliente)
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            print("Saliendo del programa")
            break
        case _:
            print("Opción desconocida")