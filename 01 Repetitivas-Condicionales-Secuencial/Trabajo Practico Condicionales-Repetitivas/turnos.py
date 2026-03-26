lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
turnos_lunes = 0
turnos_martes = 0

print("Gestion de turnos para atención al público")
operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    print("El nombre del operador debe contener solo letras y no puede estar vacío.")
    operador = input("Ingrese el nombre del operador: ")
operador = operador.capitalize()

print(f"Bienvenido, {operador}.")

while True:
    print("\nOpciones:")
    print("1. Asignar turno")
    print("2. Cancelar Turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Resumen General")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3", "4", "5"]:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        while not nombre_cliente.isalpha():
            print("El nombre del cliente debe contener solo letras y no puede estar vacío.")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
        nombre_cliente = nombre_cliente.capitalize()

        dia_elegido = input("Ingrese el día para asignar el turno (1=Lunes, 2=Martes): ")
        while not dia_elegido.isdigit() or dia_elegido not in ["1", "2"]:
            print("Día no válido. Ingrese 1 para Lunes o 2 para Martes.")
            dia_elegido = input("Ingrese el día para asignar el turno (1=Lunes, 2=Martes): ")

        if dia_elegido == "1":
            if lunes1 == "" or lunes2 == "" or lunes3 == "" or lunes4 == "":
                if lunes1 == "":
                    lunes1 = nombre_cliente
                elif lunes2 == "":
                    lunes2 = nombre_cliente
                elif lunes3 == "":
                    lunes3 = nombre_cliente
                elif lunes4 == "":
                    lunes4 = nombre_cliente
                turnos_lunes += 1
                print(f"Turno asignado para {nombre_cliente} el Lunes.")
            else:
                print("No hay más turnos disponibles para el Lunes.")

        elif dia_elegido == "2":
            if martes1 == "" or martes2 == "" or martes3 == "":
                if martes1 == "":
                    martes1 = nombre_cliente
                elif martes2 == "":
                    martes2 = nombre_cliente
                elif martes3 == "":
                    martes3 = nombre_cliente
                turnos_martes += 1
                print(f"Turno asignado para {nombre_cliente} el Martes.")
            else:
                print("No hay más turnos disponibles para el Martes.")

    elif opcion == "2":
        nombre_cancelar = input("Ingrese el nombre del cliente para cancelar el turno: ")
        while not nombre_cancelar.isalpha():
            print("El nombre debe contener solo letras y no puede estar vacío.")
            nombre_cancelar = input("Ingrese el nombre del cliente para cancelar el turno: ")
        nombre_cancelar = nombre_cancelar.capitalize()

        if nombre_cancelar == lunes1 or nombre_cancelar == lunes2 or nombre_cancelar == lunes3 or nombre_cancelar == lunes4:
            if nombre_cancelar == lunes1:
                lunes1 = ""
            elif nombre_cancelar == lunes2:
                lunes2 = ""
            elif nombre_cancelar == lunes3:
                lunes3 = ""
            elif nombre_cancelar == lunes4:
                lunes4 = ""
            turnos_lunes -= 1
            print(f"Turno cancelado para {nombre_cancelar}.")
        elif nombre_cancelar == martes1 or nombre_cancelar == martes2 or nombre_cancelar == martes3:
            if nombre_cancelar == martes1:
                martes1 = ""
            elif nombre_cancelar == martes2:
                martes2 = ""
            elif nombre_cancelar == martes3:
                martes3 = ""
            turnos_martes -= 1
            print(f"Turno cancelado para {nombre_cancelar}.")
        else:
            print(f"No se encontró un turno asignado para {nombre_cancelar}.")

    elif opcion == "3":
        dia_ver = input("¿Qué día desea ver? (1=Lunes, 2=Martes): ")
        while not dia_ver.isdigit() or dia_ver not in ["1", "2"]:
            print("Día no válido. Ingrese 1 para Lunes o 2 para Martes.")
            dia_ver = input("¿Qué día desea ver? (1=Lunes, 2=Martes): ")

        if dia_ver == "1":
            print("\nAgenda del Lunes:")
            print(f"  Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"  Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"  Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"  Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia_ver == "2":
            print("\nAgenda del Martes:")
            print(f"  Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"  Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"  Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == "4":
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes

        print("\nResumen General:")
        print(f"  Lunes   → Ocupados: {ocupados_lunes} | Disponibles: {libres_lunes}")
        print(f"  Martes  → Ocupados: {ocupados_martes} | Disponibles: {libres_martes}")

        if ocupados_lunes > ocupados_martes:
            print(f"  Día con más turnos: Lunes ({ocupados_lunes} turnos)")
        elif ocupados_martes > ocupados_lunes:
            print(f"  Día con más turnos: Martes ({ocupados_martes} turnos)")
        else:
            print(f"  Empate: ambos días tienen {ocupados_lunes} turnos")

    elif opcion == "5":
        print("Saliendo del sistema de gestión de turnos. ¡Hasta luego!")
        break