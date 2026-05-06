herramientas = []
existencias = []

while True:
    print("\n ------------Menú------------")
    print("\nOpción 1: Carga Inicial de Herramientas")
    print("\nOpción 2: Carga de Existencias")
    print("\nOpción 3: Visualización de Inventario")
    print("\nOpción 4: Consulta de Stock")
    print("\nOpción 5: Reporte de Agotados")
    print("\nOpción 6: Alta de Nuevo Producto")
    print("\nOpción 7: Actualización de Stock (Venta/Ingreso)")
    print("\nOpción 8: Salir")
    print("\n --------Fin del menú--------")

    opcion = input("Ingrese la opción que desee procesar ")
    while not opcion.isdigit():
        print("Error, ingrese solo numeros")
        opcion = input("Ingrese la opción que desee procesar ")
    opcion = int(opcion)

    match opcion:
        case 1:
            print("Carga inicial")

            cantidad = input("Ingrese la cantidad de herramientas a guardar ")
            while not cantidad.isdigit():
                print("Error, ingrese solo numeros")
                cantidad = input("Ingrese la cantidad de herramientas a guardar ")
            cantidad = int(cantidad)

            for i in range(cantidad):
                herramienta = input("Ingrese el nombre de la herramienta ").capitalize()
                while not herramienta.isalpha() or herramienta in herramientas:
                    if not herramienta.isalpha():
                        print("Error, ingrese solo letras")
                    elif herramienta in herramientas:
                        print("Error, ya existe en la lista")
                    herramienta = input("Ingrese el nombre de la herramienta ").capitalize()

                herramientas.append(herramienta)
                existencias.append(0)

                print(f"Herramienta ingresada {herramienta}, con 0 existencias")

            
            pass
        case 2:

            print("Carga de existencias")
            for i in range (len(herramientas)):
                print(herramientas[i], existencias[i])

                cambio = input("Desea cambiar la cantidad de existencias de la herramienta? (S/N) ").upper()

                while cambio != "S" and cambio != "N":
                    print("Error, ingrese solo S o N")
                    cambio = input("Desea cambiar la cantidad de existencias de la herramienta? (S/N) ").upper()

                if cambio == "S":
                    print("Cambiando la cantidad de existencias")

                    numero = input("Ingrese la cantidad de existencias a cargar ")

                    while not numero.isdigit():
                        print("Error, ingrese solo numeros")
                        numero = input("Ingrese la cantidad de existencias a cargar ")

                    numero = int(numero)

                    while numero <= 0:
                        print("Error, debe ser mayor a cero")
                        numero = input("Ingrese la cantidad de existencias a cargar ")

                        while not numero.isdigit():
                            print("Error, ingrese solo numeros")
                            numero = input("Ingrese la cantidad de existencias a cargar ")


                    existencias.pop(i)
                    existencias.insert(i, numero)
                    print(f"Cantidad de herramientas cargada como {numero}")

                else:

                    print("Okey, continue")
                    
            pass
        case 3:

            print("Visualizacion de Inventario")

            for i in range(len(herramientas)):
                print(f"{herramientas[i]}, existencias {existencias[i]}")
            pass
        case 4:
            print("Consulta de stock")
            print(", ".join(herramientas))
            
            nombre = input("Ingrese el nombre de la herramienta ").capitalize()
            while not nombre.isalpha():
                print("Error, ingrese solo texto")
                nombre = input("Ingrese el nombre de la herramienta ").capitalize()

            while not nombre in herramientas:
                print("Error, la herramienta no existe")
                nombre = input("Ingrese el nombre de la herramienta ").capitalize()

            indice = herramientas.index(nombre)

            print(f"{nombre}, existencias: {existencias[indice]}")

            pass
        case 5:
            print("Reporte de agotados")
            for i in range(len(existencias)):
                if existencias[i] == 0:
                    print(f"{herramientas[i]}, {existencias[i]}")
            pass
        case 6:
            print("Ingresar nuevo producto")
            
            nombre_dos = input("Ingrese el nombre de la herramienta a ingresar ").capitalize()
            while not nombre_dos.isalpha() or nombre_dos in herramientas:
                if not nombre_dos.isalpha():
                    print("Error, ingrese solo letras")
                elif nombre_dos in herramientas:
                    print("Error, ya existe en la lista")
                nombre_dos = input("Ingrese el nombre de la herramienta a ingresar ").capitalize()

            herramientas.append(nombre_dos)
            existencias.append(0)

            print(f"Herramienta ingresada como {nombre_dos} con 0 existencias, debe cambiar eso")
            pass
        case 7:
            print("Actualización de stock")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]}, existencias {existencias[i]}")
            
            
            nombre_tres = input("Ingrese el nombre de la herramienta a actualizar stock ").capitalize()
            while not nombre_tres.isalpha():
                print("Error, ingrese solo texto")
                nombre_tres = input("Ingrese el nombre de la herramienta a actualizar stock ").capitalize()

            while not nombre_tres in herramientas:
                print("Error, la herramienta no existe")
                nombre_tres = input("Ingrese el nombre de la herramienta a actualizar stock ").capitalize()

            indice = herramientas.index(nombre_tres)
            
            

            venta_ing = input("Desea ingresar o vender producto (I/V) ").upper()
            while venta_ing != "V" and venta_ing != "I":
                print("Error, ingrese solo V o I")
                venta_ing = input("Desea ingresar o vender producto (I/V) ").upper()

            if venta_ing == "V":
                print("Vendiendo productos")
                
                cantidad = input("Ingrese la cantidad a vender ")
                while not cantidad.isdigit():
                    print("Error, ingrese solo numeros")
                    cantidad = input("Ingrese la cantidad a vender ")
                cantidad = int(cantidad)

                producto = existencias[indice]

                resta = producto - cantidad
                while resta < 0:
                    print(resta)
                    print("Error, no puede vender mas de lo que tiene")
                    
                    cantidad = input("Ingrese la cantidad a vender ")
                    while not cantidad.isdigit():
                        print("Error, ingrese solo numeros")
                        cantidad = input("Ingrese la cantidad a vender ")
                    cantidad = int(cantidad)
                    resta = producto - cantidad

                existencias.pop(indice)
                existencias.insert(indice, resta)

                print(f"Venta realizada, existencias restantes {existencias[indice]}")
            
            else:
                print("Ingresando productos")

                
                cantidad = input("Ingrese la cantidad a ingresar ")
                while not cantidad.isdigit():
                    print("Error, ingrese solo numeros")
                    cantidad = input("Ingrese la cantidad a ingresar ")
                cantidad = int(cantidad)

                suma = existencias[indice] + cantidad


                existencias.pop(indice)
                existencias.insert(indice, suma)

                print(f"Productos ingresados, stock actual {suma}")


            pass
        case 8:
            print("Saliendo del programa")
            break
        case _:
            print("Opción desconocida")
            pass