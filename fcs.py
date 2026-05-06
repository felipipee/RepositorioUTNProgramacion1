def menu():
    print("\n ------------Menú------------")
    print("\nOpción 1: Agregar habitación")
    print("\nOpción 2: Mostrar todas las habitaciones")
    print("\nOpción 3: Consultar una habitación ")
    print("\nOpción 4: Cambiar estado de una habitación")
    print("\nOpción 5: Listar habitaciones libres u ocupadas")
    print("\nOpción 6: Salir")
    print("\n --------Fin del menú--------")

def caso1(habitaciones):
    while True:
        try:
            numero = int(input("Ingrese el número de habitación "))
            estado = input("Ingrese el estado de la habitación (libre (0) u ocupada) (1)")
            if estado not in ["0", "1"]:
                print("Estado no válido, por favor ingrese '0' u '1'")
                continue
            habitaciones.append({"numero": numero, "estado": estado})
            print(f"Habitación {numero} agregada con estado {estado}")
            break
        except ValueError:
            print("Número de habitación no válido, por favor ingrese un número")
        except Exception as e:
            print(f"Ocurrió un error: {e}")


def caso2(habitaciones):
    if not habitaciones:
        print("No hay habitaciones registradas")
        return
    for habitacion in habitaciones:
        print(f"Habitación {habitacion['numero']}: {habitacion['estado']}")

def caso3(habitaciones):
    try:
        numero = int(input("Ingrese el número de habitación a consultar "))
        for habitacion in habitaciones:
            if habitacion["numero"] == numero:
                print(f"Habitación {numero}: {habitacion['estado']}")

        print(f"No se encontró la habitación {numero}")
    except ValueError:
        print("Número de habitación no válido, por favor ingrese un número")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


def caso4(habitaciones):
    while True:
        try:
            numero = int(input("Ingrese el número de habitación a cambiar de estado "))
            for habitacion in habitaciones:
                if habitacion["numero"] == numero:
                    nuevo_estado = input("Ingrese el nuevo estado de la habitación (libre (0) u ocupada (1)) ").lower()
                    if nuevo_estado not in ["0", "1"]:
                        print("Estado no válido, por favor ingrese '0' u '1'")
                    habitacion["estado"] = nuevo_estado
                    print(f"Habitación {numero} actualizada a estado {nuevo_estado}")
                    break
            print(f"No se encontró la habitación {numero}")
        except ValueError:
            print("Número de habitación no válido, por favor ingrese un número")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

def caso5(habitaciones):
    estado = input("Ingrese el estado de las habitaciones a listar (libre u ocupada) ").lower()
    if estado not in ["libre", "ocupada"]:
        print("Estado no válido, por favor ingrese 'libre' u 'ocupada'")
        return
    habitaciones_filtradas = [habitacion for habitacion in habitaciones if habitacion["estado"] == estado]
    if not habitaciones_filtradas:
        print(f"No hay habitaciones {estado}")
        return
    for habitacion in habitaciones_filtradas:
        print(f"Habitación {habitacion['numero']}: {habitacion['estado']}")