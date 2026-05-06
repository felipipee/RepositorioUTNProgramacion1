
herramientas = []
existencias = []

while True:
    print("\n ------------Menú------------")
    print("\nOpción 1: Carga masiva")
    print("\nOpción 2: Carga de Existencias")
    print("\nOpción 3: Visualización de Inventario")
    print("\nOpción 4: Consulta de Stock")
    print("\nOpción 5: Reporte de Agotados")
    print("\nOpción 6: Alta de Nuevo Producto")
    print("\nOpción 7: Actualización de Stock")
    print("\nOpción 8: Salir")
    print("\n --------Fin del menú--------")

    opcion = input("Ingrese la opción que desee procesar ")
    while not opcion.isdigit():
        print("Error, ingrese solo numeros")
        opcion = input("Ingrese la opción que desee procesar ")
    opcion = int(opcion)

    match opcion:
        case 1:
            print("Carga Masiva")
            cantidad = input("Ingrese la cantidad de herramientas a cargar ")
            while not cantidad.isdigit():
                print("Error, ingrese solo numeros")
                cantidad = input("Ingrese la cantidad de herramientas a cargar ")
            cantidad = int(cantidad)

            for i in range(cantidad):
                print(f"Ingresando {cantidad} herramienta/s ")

                nombre_herramienta = input("Ingrese el nombre de la herramienta ").capitalize()
                while not nombre_herramienta.isalpha():
                    print("Error, ingrese solo texto")
                    nombre_herramienta = input("Ingrese el nombre de la herramienta ").capitalize()

                while nombre_herramienta in herramientas:
                    print("Esa herramienta ya esta cargada")
                    nombre_herramienta = input("Ingrese el nombre de la herramienta ").capitalize()
                
                herramientas.append(nombre_herramienta)
                existencias.append(0)

                print(f"Herramienta ingresada como {nombre_herramienta}, con 0 existencias, debe cambiar esto en la opcion 2")
            pass
        case 2:
            print("Carga de existencias")
            for j in range(len(herramientas)):
                indice = herramientas[j]
                print(f"Herramienta {herramientas[j]}")
                cambio = input("Ingrese S/N ").upper()
                while cambio != "S" and cambio != "N":
                    print("Error, ingrese solo S o N")
                    cambio = input("Ingrese S/N ").upper()
                
                if cambio == "S":
                    print("Cambiando la cantidad de existencias")
                    numero = input("Ingrese la cantidad de existencias a ingresar ")

                    while not numero.isdigit():
                        print("Error, ingrese solo numeros")
                        numero = input("Ingrese la cantidad de existencias a ingresar ")
                    numero = int(numero)
                    while numero <= 0:
                        print("Error, debe ser mayor a cero")
                        numero = input("Ingrese la cantidad de existencias a ingresar ")
                        while not numero.isdigit():
                            print("Error, ingrese solo numeros")
                            numero = input("Ingrese la cantidad de existencias a ingresar ")
                        numero = int(numero)

                    existencias.pop(indice)
                    existencias.insert(indice, numero)
                    print(f"La herramienta {herramientas[indice]}, ha sido cargada con {numero}")
                
                else:
                    print(f"Se mantiene con {existencias[indice]}")
                
            pass
        case 3:
            for i in range(len(herramientas)):
                print(f"{herramientas[i]}: {existencias[i]}")
            pass
        case 4:
            print("Consultando el stock")
            print(", ".join(herramientas))
            herramienta = input("Ingrese la herramienta a consultar el stock o si quiere salir(Salir): ").capitalize()
            if herramienta == "Salir":
                print("Saliendo de la opcion 4")
                pass
            while not herramienta.isalpha():
                print("Error, ingrese solo texto")
                herramienta = input("Ingrese la herramienta a consultar el stock ")
            while not herramienta in herramientas:
                print("Esa herramienta no existe")
                herramienta = input("Ingrese la herramienta a consultar el stock ")

            k = herramientas.index(herramienta)

            print(f"{herramienta}: {existencias[k]}")

            pass
        case 5:
            for i in range(len(herramientas)):
                if existencias[i] == 0:
                    print(f"{herramientas[i]}, existencias: {existencias[i]}")
            pass
        case 6:
            print("Alta del nuevo producto")
            nombre = input("Ingrese el nombre de la herramienta ").capitalize()
            while not nombre.isalpha():
                print("Error, ingrese solo texto")
                nombre = input("Ingrese el nombre de la herramienta ").capitalize()
            
            cambiar = input("Desea ingresar existencias? S/N").upper()
            while cambiar != "S" and cambiar != "N":
                print("Error, ingrese solo S o N")
                cambiar = input("Desea ingresar existencias? S/N").upper()
            
            if cambiar == "S":
                cant = input("Ingrese la cantidad de existencias a cargar: ")
                while not cant.isdigit():
                    print("Error, ingrese solo numeros")
                    cant = input("Ingrese la cantidad de existencias a cargar: ")
                cant = int(cant)

                herramientas.append(nombre)
                existencias.append(cant)
                print(f"Herramienta cargada como {nombre}, con {cant} existencias ")
            
            else:
                print("Ok, con 0 existencias")

                herramientas.append(nombre)
                existencias.append(0)
            
            pass
        case 7:
            herramienta = input("Ingrese la herramienta a consultar el stock o si quiere salir(Salir): ").capitalize()
            if herramienta == "Salir":
                print("Saliendo de la opcion 7")
                pass
            while not herramienta.isalpha():
                print("Error, ingrese solo texto")
                herramienta = input("Ingrese la herramienta a consultar el stock ")
            while not herramienta in herramientas:
                print("Esa herramienta no existe")
                herramienta = input("Ingrese la herramienta a consultar el stock ")

            indice = herramientas.index(herramienta)

            vender_ingresar = input("Desea vender o Ingresar productos (V/I)").upper()
            while vender_ingresar != "V" and vender_ingresar != "I":
                print("Error, ingrese solo S o N")
                vender_ingresar = input("Desea vender o Ingresar productos (V/I)").upper()
            
            if vender_ingresar == "V":
                print("Vendiendo")
                
                cant_vender = input("Ingrese la cantidad de existencias a vender ")
                while not cant_vender.isdigit():
                    print("Error, ingrese solo numeros")
                    cant_vender = input("Ingrese la cantidad de existencias a vender ")
                cant_vender = int(cant_vender)

                resta = herramientas[indice] - cant_vender

                while resta < 0:
                    print("No puede vender mas de lo que tiene! ")
                    cant_vender = input("Ingrese la cantidad de existencias a vender ")
                
                herramientas.pop(indice)
                herramientas.insert(indice, herramienta)

                print(f"Herramienta/s vendida/s {cant_vender}, existencias restantes: {existencias[indice]}")

            else:
                
                cant_sum = input("Ingresa la cantidad de existencias a ingresar: ")
                while not cant_sum.isdigit():
                    print("Error, ingrese solo numeros")
                    cant_sum = input("Ingresa la cantidad de existencias a ingresar: ")
                cant_sum = int(cant_sum)

                suma = herramientas[indice] + cant_sum

                existencias.pop(indice)
                existencias.insert(indice, suma)

                print(f"Existencias actualizadas por {suma}")
            pass
        case 8:
            print("Saliendo del programa")
            break
        case _:
            print("Opción desconocida")


