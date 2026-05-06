pre_hab = "Habitación "
l = "Libre"
o = "Ocupada"
habitaciones = []
estados = []
libre_ocupada = []

while True:
    print("1. Ingresar números de habitación: (Registrar las habitaciones del hotel)")
    print("2. Ingresar estados (0/1) paralelos: (Definir el estado inicial de cada habitación)")
    print("3. Mostrar estado general: (Mostrar el estado de todas las habitaciones)")
    print("4. Consultar estado de una habitación: (Verificar el estado de una habitación específica)")
    print("5. Listar ocupadas o libres (según lo que se pida)")
    print("6. Agregar habitación: (Añadir una nueva habitación al sistema)")
    print("7. Cambiar estado: (Cambiar el estado de una habitación)")
    print("8. Salir: (Terminar el programa) \n")

    option = input("Ingrese la opcion a procesar ")
    while not option.isdigit():
        print("Error, ingrese un numero")
        option = input("Ingrese la opcion a procesar ")
    option = int(option)

    match option:
        case 1:
            cantidad = input("Ingrese la cantidad de habitaciones a ingresar ")
            while not cantidad.isdigit():
                print("Error")
                cantidad = input("Ingrese la cantidad de habitaciones a ingresar ")
            cantidad = int(cantidad)
            while cantidad < 1:
                print("Error, no puede ingresar 0 habitaciones")
                cantidad = input("Ingrese la cantidad de habitaciones a ingresar ")
            cantidad = int(cantidad)
            for i in range(cantidad):
                print(f"Habitación {i+1}")
                numero = input("Ingrese el numero de habitacion")
                while not numero.isdigit():
                    print("Error, ingrese solo numeros")
                    numero = input("Ingrese el numero de habitacion")
                habitacion_completa = pre_hab + numero + ": "
                habitaciones.append(habitacion_completa)
                estados.append(0)
                libre_ocupada.append(o)
                print("Habitacion guardada con exito, con estado Libre")
            pass
        case 2:
            print("Ingresar estados")
            for i in range(len(habitaciones)):
                print(f"{habitaciones[i]}")
                print(f"Estado actual {habitaciones[i]}{libre_ocupada[i]}")
                cambiar = input("Desea cambiar el estado(s o n): ")
                while cambiar != "s" and cambiar != "n":
                    print("Error, ingrese s o n")
                    cambiar = input("Desea cambiar el estado(s o n): ")
                if cambiar == "s":
                    print("Cambiar estado")
                    if estados[i] == 0:
                        print("Cambiando estado de Libre a Ocupada")
                        estados.pop[i]
                        estados.insert([i], 1)
                        print("Estado cambiado a Ocupada")
                    else:
                        if estados[i] == 1:
                            print("Cambiando estado de Ocupada a Libre")
                            estados.pop[i]
                            estados.insert([i], 1)
                            print("Estado cambiado de Ocupada a Libre")
                else:
                    pass
            pass
        case 3:
            for i in range(len(habitaciones)):
                print(f"{habitaciones[i]}{libre_ocupada[i]}")
            pass
        case 4:
            for i in range(len(habitaciones)):
                print(f"{habitaciones[i]} {libre_ocupada[i]}")
            consulta = input("Ingrese el numero de habitacion ")
            while not consulta.isdigit():
                print("Error")
                consulta = input("Ingrese el numero de habitacion ")
            habitacion_completa = pre_hab + consulta + ": "
            while not habitacion_completa in habitaciones:
                print("Error")
                consulta = input("Ingrese el numero de habitacion ")
            habitacion_completa = pre_hab + consulta + ": "
            indice = habitaciones.index(habitacion_completa)
            print(f"{habitacion_completa} {libre_ocupada[indice]}")
            pass
        case 5:
            print("Habitaciones libres o ocupadas")
            requerimentos = input("Quiere ver las habitaciones libres o ocupadas(L, O) ").upper()
            while not requerimentos.isalpha:
                print("Error")
                requerimentos = input("Quiere ver las habitaciones libres o ocupadas(L, O) ").upper()
            while requerimentos != "L" and requerimentos != "O":
                print("Error") 
                requerimentos = input("Quiere ver las habitaciones libres o ocupadas(L, O) ").upper()
            if requerimentos == "L":
                print("Buscando las habitaciones libres")
                for i in range(len(estados)):
                    if estados[i] == 0:
                        print(f"{habitaciones[i]} {libre_ocupada[i]}")
                    else:
                        print(f"{habitaciones[i]} {libre_ocupada[i]}")
            pass
        case 6:
            print("Agregar nueva habitación")
            numero = input("Ingrese el numero de habitacion")
            while not numero.isdigit():
                    print("Error, ingrese solo numeros")
                    numero = input("Ingrese el numero de habitacion")
            habitacion_completa = pre_hab + numero + ": "
            habitaciones.append(habitacion_completa)
            estados.append(0)
            libre_ocupada.append(o)
            pass
        case 7:
            print("Cambiando el estado de habitación")
            for i in range(len(habitaciones)):
                print(f"{habitaciones[i]}{libre_ocupada[i]}")
            numero = input("Ingrese el número de habitacion")
            while not numero.isdigit():
                print("Error, ingrese un numero que este ne las habitaciones")
                numero = input("Ingrese el número de habitacion")
            habitacion_completa = pre_hab + numero + ": "
            i = habitaciones.index(habitacion_completa)
            cambiar = input("Desea cambiar el estado(s o n): ")
            while cambiar != "s" and cambiar != "n":
                print("Error, ingrese s o n")
                cambiar = input("Desea cambiar el estado(s o n): ")
            if cambiar == "s":
                print("Cambiar estado")
                if estados[i] == 0:
                    print("Cambiando estado de Libre a Ocupada")
                    estados.pop[i]
                    estados.insert([i], 1)
                    print("Estado cambiado a Ocupada")
                else:
                    if estados[i] == 1:
                        print("Cambiando estado de Ocupada a Libre")
                        estados.pop[i]
                        estados.insert([i], 1)
                        print("Estado cambiado de Ocupada a Libre")
            else:
                pass
            pass
        case 8:
            print("Saliendo del programa")
            break
            
        case _:
            print("Opcion desconocida")
            pass