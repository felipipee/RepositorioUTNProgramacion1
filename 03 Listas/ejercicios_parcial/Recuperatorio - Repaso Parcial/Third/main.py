herramientas = []
existencias = []

while True:
    print("\n ------------Menú------------")
    print("\nOpción 1: Carga herramientas")
    print("\nOpción 2: Carga Existencias")
    print("\nOpción 3: Ver resumen de productos")
    print("\nOpción 4: Consulta de stock por herramienta")
    print("\nOpción 5: Reporte de Agotados")
    print("\nOpción 6: Nuevo producto")
    print("\nOpción 7: Ingresos y Ventas")
    print("\nOpción 8: Salir")
    print("\n --------Fin del menú--------")

    opcion = input("Ingrese la opción que desee procesar ")
    while not opcion.isdigit():
        print("Error, ingrese solo numeros")
        opcion = input("Ingrese la opción que desee procesar ")
    opcion = int(opcion)

    match opcion:
        case 1:
            print("Carga de herramientas")
            

            cantidad = input("Ingrese la cantidad de herramientas a guardar ")
            while not cantidad.isdigit():
                print("Error, ingrese solo numeros")
                cantidad = input("Ingrese la cantidad de herramientas a guardar ")
            cantidad = int(cantidad)

            for i in range(cantidad):
                print(f"Cargando herraminta {i}")

                

                nombre = input("Ingrese el nombre de la herramienta").capitalize()

                while not nombre.isalpha() or nombre in herramientas:

                    if not nombre.isalpha():
                        print("Error, ingrese solo letras")

                    elif nombre in herramientas:
                        print("Error, ya existe en la lista")

                    nombre = input("Ingrese el nombre de la herramienta").capitalize()

                herramientas.append(nombre)
                existencias.append(0)

                print(f"Herramienta ingresada como {nombre}, con 0 existencias, debe cambiarlo en la opción 2")
            pass
        case 2:

            print("Cargando existencias")

            for i in range(len(herramientas)):
                print(f"{herramientas[i]}, existencias {existencias[i]}")

            
                cambiar = input("Desea cambiar la cantidad de existencias? (S/N) ").upper()

                while cambiar != "S" and cambiar != "N":
                    print("Error, ingrese solo S o N")
                    cambiar = input("Desea cambiar la cantidad de existencias? (S/N) ").upper()

                if cambiar == "S":
                    print("Cambiando existencias")


                    numero = input("Ingrese la cantidad de existencias a guardar ")

                    while not numero.isdigit():
                        print("Error, ingrese solo numeros")
                        numero = input("Ingrese la cantidad de existencias a guardar ")

                    numero = int(numero)

                    while numero <= 0:
                        print("Error, debe ser mayor a cero")
                        numero = input("Ingrese la cantidad de existencias a guardar ")

                        while not numero.isdigit():
                            print("Error, ingrese solo numeros")
                            numero = input("Ingrese la cantidad de existencias a guardar ")

                        numero = int(numero)

                    existencias.pop(i)
                    existencias.insert(i, numero)

                else:
                    print("Okey, continua")
                    
            pass
        case 3:
            print("Herramientas  Existencias")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]}      {existencias[i]}")
            pass
        case 4:
            print("Consultando stock por nombre")
            print(", ".join(herramientas))

            nombre = input("Ingrese el nombre de la herramienta a consultar").capitalize()

            while not nombre.isalpha():
                print("Error, ingrese solo texto")
                nombre = input("Ingrese el nombre de la herramienta a consultar").capitalize()

            while not nombre in herramientas:
                print("Error, esa herramienta no existe")
                nombre = input("Ingrese el nombre de la herramienta a consultar").capitalize()

            indice = herramientas.index(nombre)

            print(f"{herramientas[indice]}, existencias {existencias[indice]}")
            pass
        case 5:
            print("Reporte de agotados")

            for i in range(len(existencias)):
                if existencias[i] == 0:
                    print(f"{herramientas[i]}, existecias {existencias[i]}")
            pass
        case 6:
            print("Nuevo producto")

            

            nombre = input("Ingrese el nombre de la nueva herramienta ").capitalize()

            while not nombre.isalpha() or nombre in herramientas:

                if not nombre.isalpha():
                    print("Error, ingrese solo letras")
                    pass
                
                elif nombre in herramientas:
                    print("Error, ya existe en la lista")
                    pass

                nombre = input("Ingrese el nombre de la nueva herramienta ").capitalize()

            herramientas.append(nombre)
            existencias.append(0)

            print(f"Herramienta ingresada como {nombre}, con 0 existencias")
            pass
        case 7:
            print("Actualizacion de stock")

            print(", ".join(herramientas))

            

            nombre = input("Ingrese el nombre de la herrramienta ").capitalize()

            while not nombre.isalpha():
                print("Error, ingrese solo texto")
                nombre = input("Ingrese el nombre de la herrramienta ").capitalize()

            while not nombre in herramientas:
                print("Error, herramienta desconocida")
                nombre = input("Ingrese el nombre de la herrramienta ").capitalize()

            indice = herramientas.index(nombre)
            print(f"{nombre}, tiene {existencias[indice]} existencias")

                

            ven_ing = input("Desea Vender o ingresar productos (V/I): ").upper()

            while ven_ing != "V" and ven_ing != "I":
                print("Error, ingrese solo S o N")
                ven_ing = input("Desea Vender o ingresar productos (V/I): ").upper()

            if ven_ing == "V":
                print("Vendiendo")

                numero = input("Ingrese la cantidad de existencias a vender")
                while not numero.isdigit():
                    print("Error, ingrese solo numeros")
                    numero = input("Ingrese la cantidad de existencias a vender")

                numero = int(numero)

                resta = existencias[indice] - numero

                while resta < 0:

                    print("No puede vender mas de lo que tiene")

                    numero = input("Ingrese la cantidad de existencias a vender")

                    resta = existencias[indice] - numero



                    while not numero.isdigit():
                        print("Error, ingrese solo numeros")
                        numero = input("Ingrese la cantidad de existencias a vender")


                numero = int(numero)
                resta = existencias[indice] - numero

                existencias.pop(indice)
                existencias.insert(indice, resta)

            else:

                numero = input("Ingrese la cantidad de herramientas a ingresar ")
                while not numero.isdigit():
                    print("Error, ingrese solo numeros")
                    numero = input("Ingrese la cantidad de herramientas a ingresar ")
                numero = int(numero)
                suma = existencias[indice] + numero
                existencias.pop(indice)
                existencias.insert(indice, suma)

                


            pass
        case 8:
            print("Saliendo del programa")
            break
        case _:
            print("Opción desconocida")