

pre_orden = "ORD-"
ordenes = []
horas_estimado = []

while True:
    print("1. Ingresar órdenes (códigos): (Registrar las órdenes de reparación en el sistema) "),
    print("2. Ingresar horas estimadas por orden: (Definir el tiempo estimado inicial para cada orden) "),
    print("3. Mostrar agenda del taller: (Mostrar todas las órdenes y sus tiempos estimados)"),
    print("4. Consultar horas por orden: (Verificar el tiempo estimado para una orden específica)"),
    print("5. Listar órdenes con 0 horas (pendiente de diagnóstico): (Mostrar las órdenes que requieren diagnóstico) "),
    print("6. Agregar orden: (Añadir una nueva orden al sistema) "),
    print("7. Actualizar horas: (Modificar el tiempo estimado de una orden)"),
    print("8. Salir del programa (Termina la ejecución)")


    opcion = input("Ingrese la opcion a ingresar ")
    while not opcion.isdigit():
        print("Error, solo números")
        opcion = input("Ingrese la opcion a ingresar ")
    opcion = int(opcion)

    match (opcion):
        case 1:
            print("Ingresando ordenes")
            numero_ordenes = input("Cuantas ordenes desea ingresar? ")
            while not numero_ordenes.isdigit():
                print("Error, ingrese solo numeros")
                numero_ordenes = input("Cuantas ordenes desea ingresar? ")
            numero_ordenes = int(numero_ordenes)
            for i in range(numero_ordenes):
                print(f"Orden numero {i+1}")
                orden = input("Ingrese el numero de orden")
                while not orden.isdigit():
                    print("Error")
                    orden = input("Ingrese el numero de orden)")
                orden = str(orden)
                orden = orden.zfill(3)
                orden_completa = pre_orden + orden
                duracion = "0.0 hs"
                ordenes.append(orden_completa)
                horas_estimado.append(duracion)
                print(f"Orden guardada como: {orden_completa}, con una duracion estimada de {duracion}")

                print(orden_completa)
                
                pass
        case 2:
            indice = len(ordenes)
            for i in range(indice):
                print(f"Opcion {ordenes[i]}, Duracion {horas_estimado[i]}")
                cambiar = input("Quiere cambiar el horario? (s o n) ")
                while cambiar != "s" and cambiar != "n":
                    print("Error")
                    cambiar = input("Quiere cambiar el horario? (s o n) ")
                if cambiar == "s":
                    print("Cambiando el tiempo estimado")
                    tiempo_nuevo = input("Ingrese el tiempo estimado nuevo ")
                    while not tiempo_nuevo.replace(".", "", 1).isdigit() or float(tiempo_nuevo) < 0:
                        print("Error")
                        tiempo_nuevo = input("Ingrese el tiempo estimado nuevo ")
                    tiempo_nuevo = str(tiempo_nuevo)
                    tiempo_nuevo_completo = tiempo_nuevo + " hs"
                    horas_estimado.pop(i)
                    horas_estimado.insert(i, tiempo_nuevo_completo)
                else:
                    pass
                    
            pass
        case 3:
            print(f", ".join(ordenes))
            print(f", ".join(horas_estimado))
            pass
        case 4:
            print("Consultar tiempo estimado por orden")
            print(", ".join(ordenes))
            orden = input("Ingrese el numero de orden que quiere consultar")
            while not orden.isdigit:
                print("Error")
                orden = input("Ingrese el numero de orden que quiere consultar")
            orden = orden.zfill(3)
            orden_completo = pre_orden + orden
            while orden_completo not in ordenes:
                print("Error, ese numero no es una orden")
                orden = input("Ingrese el numero de orden que quiere consultar")
            indice = ordenes.index(orden_completo)
            hora = horas_estimado[indice]
            print((orden_completo))
            print((hora))

            pass
        case 5:
            print("Listando ordenes sin horas descriptas")

            for i in range(len(ordenes)):
                if horas_estimado[i] == "0.0 hs":
                    print(f"{ordenes[i]}, {horas_estimado[i]}")
                
            pass
        case 6:
            print("Agregar orden")
            orden = input("Ingrese el numero de orden")
            while not orden.isdigit():
                print("Error")
                orden = input("Ingrese el numero de orden)")
            orden = orden.zfill(3)
            orden = str(orden)
            orden_completa = pre_orden + orden
            duracion = "0.0 hs"
            ordenes.append(orden_completa)
            horas_estimado.append(duracion)
            print(f"Orden guardada como: {orden_completa}, con una duracion estimada de {duracion}")
            pass
        case 7:
            print("Cambiar el horario estimado de la orden")
            for i in range(len(ordenes)):
                print(f"{[i]}.{ordenes[i]}, {horas_estimado[i]}")
            indice = input("Ingrese la orden a modificar")
            while not indice.isdigit():
                print("Error")
                indice = input("Ingrese la orden a modificar")
            indice = int(indice)
            indice_final = indice - 1
            hora_nueva = input("Ingrese el horario nuevo")
            while not hora_nueva.replace(".", "", 1).isdigit or float(hora_nueva) < 0:
                print("Error")
                hora_nueva = input("Ingrese el horario nuevo")
            hora_nueva = str(hora_nueva)
            hora_nueva_completa = hora_nueva + " hs"
            horas_estimado.pop(indice_final)
            horas_estimado.insert(indice_final, hora_nueva_completa)
            pass
        case 8:
            print("Saliendo del programa")
            break
            
        case _:
            print("Opcion desconocida")
            pass