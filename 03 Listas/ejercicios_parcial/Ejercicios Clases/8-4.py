habitaciones = []
estados = []

while True:
    print(f"\n------------Menu-----------")
    print(f"\n 1. Ingresar numeros de habitación ")
    print(f"\n 2. Ingresar Estados")
    print(f"\n 3. Mostrar Estado General")
    print(f"\n 4. Consultar estado de una habitación")
    print(f"\n 5. Listar ocupadas o libres")
    print(f"\n 6. Agregar habitación")
    print(f"\n 7. Cambiar estado")
    print(f"\n 8. Salir")

    opcion = input("Ingrese la opción a procesar: ").strip()
    while not opcion.isdigit():
        print("Inaceptable")
        opcion = input("Ingrese la opción a procesar: ").strip()
    opcion = int(opcion)
    match (opcion):
        case 1:
            cantidad = input("Ingrese la cantidad de habitaciones a ingresar(número): ")
            while not cantidad.strip().isdigit():
                print("Inaceptable")
                cantidad = input("Ingrese la cantidad de habitaciones a ingresar(número): ")
            cantidad = int(cantidad)
            while cantidad <= 0:
                cantidad = input("No se puede ingresar un numero negativo o cero, intete nuevamente: ")
                while not cantidad.isdigit():
                    cantidad = input("Por favor, ingrese un numero entero positivo: ")
                cantidad = int(cantidad)
            for i in range(cantidad):
                habitacion = input(f"Ingrese el número de la habitacion (100, 101, ...) {i + 1} ")
                while not habitacion.isdigit():
                    print("No se puede...")
                    habitacion = input(f"Ingrese el número de la habitacion (100, 101, ...) {i + 1} ")
                habitacion = int(habitacion)
                while habitacion < 100:
                    print("No se puede...")
                    habitacion = input(f"Ingrese el número de la habitacion (100, 101, ...) {i + 1} ")
                    while not habitacion.isdigit():
                        print("No se puede...")
                        habitacion = input(f"Ingrese el número de la habitacion (100, 101, ...) {i + 1} ")
                    habitacion = int(habitacion)
                while habitacion in habitaciones:
                    print("No se puede...")
                    habitacion = input(f"Ingrese el número de la habitacion (100, 101, ...) {i + 1} ")
                habitacion = int(habitacion)
                habitaciones.append(habitacion)
                estados.append(0)
                print(f"Habitacion ingresada como {habitacion}")
            pass
        case 2:
            if not habitaciones:
                print("No hay habitaciones")
            else:
                for i in (habitaciones):
                    print(f"Habitacion {i}")
                    estado = input("Esta ocupada o libre (1 o 0)")
                    
                    while not estado.strip().isdigit():
                        print("Debe ser 1 o 0")
                        estado = input("Esta ocupada o libre (1 o 0)")
                    estado = int(estado)
                    while estado not in [0, 1]:
                        print("Debe ser 1 o 0")
                        estado = input("Esta ocupada o libre (1 o 0)")
                        while not estado.strip().isdigit():
                            print("error")
                            estado = input("Esta ocupada o libre (1 o 0)")

                        estado = int(estado)
                    estados.append(estado)
                    print(f"Estado ingresado como {estado}")




            pass
        case 3:
            if not estados:
                print("Falta ingresar estado")
            if not habitaciones or not estados:
                print("Faltan datos")
            else:
                for i in range(len(habitaciones)):
                    if estados[i] == 0:
                        print(f"Habitacion {habitaciones[i]}: Libre")
                    else:
                        print(f"Habitacion {habitaciones[i]}: Ocupadas")
            pass
        case 4:
            verificacion = input("Ingrese el número de una habitación: ").strip()

            while not verificacion.isdigit():
                print("Inaceptable.")
                verificacion = input("Ingrese el número de una habitación: ").strip()
            verificacion = int(verificacion)

            while verificacion not in habitaciones:
                print(f"La habitación {verificacion} no se encuentra en el hotel.")

                verificacion = input("Ingrese el número de una habitación: ").strip()

                while not verificacion.isdigit():
                    print("Inaceptable.")
                    verificacion = input("Ingrese el número de una habitación: ").strip()

                verificacion = int(verificacion)

            indice = habitaciones.index(verificacion)

            if estados[indice] == 0:
                print(f"Habitación {verificacion}: Libre")
            else:
                print(f"Habitación {verificacion}: Ocupada")

        case 5:
            while True:
                print("1) Ver Habitacion Libres \n" \
                "2) Ver Habitacion Ocupadas\n" \
                "3) Salir")
                opcion = input("Elija una opcion: ")

                while not opcion.isdigit():
                    print("ERROR! Ingrese un numero entero positivo")
                    opcion = input("Elija una opcion: ")

                opcion = int(opcion)

                match opcion:
                    case 1: 
                        contador = 0
                        for i in estados:
                            if i == 0:
                                print(f"Habitacion {habitaciones[contador]} -- Estado: Libre")
                            elif i == 1:
                                pass
                            contador += 1
                        break
                    case 2:
                        contador = 0
                        for i in estados:
                            if i == 1:
                                print(f"Habitacion {habitaciones[contador]} -- Estado: Ocupado")
                            elif i == 0:
                                pass
                            contador += 1
                        break
                    case 3:
                        break
                    case _:
                        print("ERROR! Ingrese un numero entre el 1-3")
                        pass
        case 6:
            agregar_habitacion = input("Ingrese el número de la habitación a agregar: ")

            while not agregar_habitacion.isdigit():
                print("Ingrese un número")
                agregar_habitacion =  input("Ingrese el número de la habitación a agregar: ")
            agregar_habitacion = int(agregar_habitacion)

            while agregar_habitacion <= 0:
                agregar_habitacion = input("No se puede ingresar un numero negativo o cero, intete nuevamente: ")

                while not agregar_habitacion.isdigit():
                    agregar_habitacion = input("Ingrese un numero entero positivo")
                agregar_habitacion = int(agregar_habitacion)

            while agregar_habitacion < 100:
                print("Error")
                agregar_habitacion = input("Ingrese el numero de la habitación (100,101,....)")

                while not agregar_habitacion.isdigit():
                    print("Error")
                    agregar_habitacion = input("Ingrese el numero de la habitación (100,101,....)")
                    
                agregar_habitacion = int(agregar_habitacion)

            if agregar_habitacion in habitaciones:
                print(f"La habitación {agregar_habitacion} ya esta en el sistema")
            else:
                estado_habitacion = input("Ingrese si la habitacion esta (libre 0/ocupada 1): ").strip().lower()
                while not estado_habitacion.isdigit():
                        print("Error")
                        estado_habitacion = input("Ingrese si la habitacion esta (libre 0/ocupada 1): ").strip().lower()
                estado_habitacion = int(estado_habitacion)

                while estado_habitacion not in [0, 1]:
                    print("No funciona, ingrese 0 o 1.")
                    estado_habitacion = input("Ingrese si la habitacion esta (libre 0/ocupada 1): ").strip().lower()
                    while not estado_habitacion.isdigit():
                        print("Error")
                        estado_habitacion = input("Ingrese si la habitacion esta (libre 0/ocupada 1): ").strip().lower()
                    estado_habitacion = int(estado_habitacion)

                print(f"La habitación {agregar_habitacion} se agrego correctamente con el estado de {estado_habitacion}")
                habitaciones.append(agregar_habitacion)
                estados.append(estado_habitacion)
            pass
        case 7:
            if not estados:
                print("Las habitaciones no tienen estados asignados")
            else:
                print(f'Que habitación desea cambiar el estado?')
                habitacion_a_cambiar = input("Ingrese el número de la habitación: ")
                while True:
                    if not habitacion_a_cambiar.isdigit():
                        print('Error, tiene que ser un numero')
                        habitacion_a_cambiar = input("Ingrese el número de la habitación: ")
                    elif int(habitacion_a_cambiar) not in habitaciones:
                        print('Error, esa habitación no existe')
                        habitacion_a_cambiar = input("Ingrese el número de la habitación: ")
                    else:
                        break
                estados_a_cambiar = input('Ingrese el nuevo estado de la habitacion (0 para libre, 1 para ocupada): ')
                while not estados_a_cambiar.isdigit() or int(estados_a_cambiar) not in [0, 1]:
                    print('Error, tiene que ser 0 o 1')
                    estados_a_cambiar = input('Ingrese el nuevo estado (0 para libre, 1 para ocupada): ')
                lugar = habitaciones.index(int(habitacion_a_cambiar))
                estados[lugar] = int(estados_a_cambiar)
            pass
        case 8:
            print(f"\nSaliendo del programa...")
            break
        case _:
            print(f"\nOpción ineceptable")
            pass
