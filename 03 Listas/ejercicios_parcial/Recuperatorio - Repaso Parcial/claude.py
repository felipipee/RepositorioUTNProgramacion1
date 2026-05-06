# =============================================
#   SISTEMA DE CONTROL DE INVENTARIO
#   Ferretería - Parcial 1 - Programación 1
#   UTN - Tecnicatura Universitaria en Programación
# =============================================

herramientas = []
existencias = []

while True:
    print("\n========================================")
    print("   SISTEMA DE INVENTARIO - FERRETERÍA")
    print("========================================")
    print("1. Carga inicial de herramientas")
    print("2. Carga de existencias")
    print("3. Visualización de inventario")
    print("4. Consulta de stock")
    print("5. Reporte de agotados")
    print("6. Alta de nuevo producto")
    print("7. Actualización de stock (Venta/Ingreso)")
    print("8. Salir")
    print("========================================")

    opcion = input("Seleccione una opción: ")

    match opcion:

        # ------------------------------------------
        # OPCIÓN 1: Carga inicial de herramientas
        # ------------------------------------------
        case "1":
            if len(herramientas) > 0:
                print("Ya existe una carga inicial. Use la opción 6 para agregar productos.")
            else:
                cantidad_valida = False
                cantidad = 0
                while not cantidad_valida:
                    entrada = input("¿Cuántas herramientas desea cargar? ")
                    if entrada.isdigit() and int(entrada) > 0:
                        cantidad = int(entrada)
                        cantidad_valida = True
                    else:
                        print("Ingrese un número entero positivo.")

                cargadas = 0
                while cargadas < cantidad:
                    nombre = input(f"Ingrese el nombre de la herramienta {cargadas + 1}: ").strip()
                    if nombre == "":
                        print("El nombre no puede estar vacío. Intente nuevamente.")
                    elif nombre in herramientas:
                        print("Esa herramienta ya fue ingresada. Intente con otro nombre.")
                    else:
                        herramientas.append(nombre)
                        existencias.append(0)
                        cargadas += 1

                print(f"\n{cantidad} herramienta(s) cargada(s) correctamente.")

        # ------------------------------------------
        # OPCIÓN 2: Carga de existencias
        # ------------------------------------------
        case "2":
            if len(herramientas) == 0:
                print("Primero debe realizar la carga inicial de herramientas (opción 1).")
            else:
                for i in range(len(herramientas)):
                    cargado = False
                    while not cargado:
                        print(f"Herramienta: {herramientas[i]}")
                        entrada = input(f"  Ingrese las existencias: ")
                        if entrada.isdigit():
                            existencias[i] = int(entrada)
                            cargado = True
                        else:
                            print("  Ingrese un número entero positivo o cero.")
                print("\nExistencias cargadas correctamente.")

        # ------------------------------------------
        # OPCIÓN 3: Visualización de inventario
        # ------------------------------------------
        case "3":
            if len(herramientas) == 0:
                print("No hay herramientas cargadas.")
            else:
                print("\n--- INVENTARIO COMPLETO ---")
                print(f"{'Herramienta':<25} {'Stock':>10}")
                print("-" * 37)
                for i in range(len(herramientas)):
                    print(f"{herramientas[i]:<25} {existencias[i]:>10}")

        # ------------------------------------------
        # OPCIÓN 4: Consulta de stock
        # ------------------------------------------
        case "4":
            if len(herramientas) == 0:
                print("No hay herramientas cargadas.")
            else:
                nombre_buscar = input("Ingrese el nombre de la herramienta a consultar: ").strip()
                encontrado = False
                for i in range(len(herramientas)):
                    if herramientas[i] == nombre_buscar:
                        print(f"\nHerramienta: {herramientas[i]}")
                        print(f"Stock disponible: {existencias[i]} unidades.")
                        encontrado = True
                if not encontrado:
                    print(f"La herramienta '{nombre_buscar}' no existe en el catálogo.")

        # ------------------------------------------
        # OPCIÓN 5: Reporte de agotados
        # ------------------------------------------
        case "5":
            if len(herramientas) == 0:
                print("No hay herramientas cargadas.")
            else:
                print("\n--- PRODUCTOS AGOTADOS ---")
                hay_agotados = False
                for i in range(len(herramientas)):
                    if existencias[i] == 0:
                        print(f"  - {herramientas[i]}")
                        hay_agotados = True
                if not hay_agotados:
                    print("No hay productos agotados.")

        # ------------------------------------------
        # OPCIÓN 6: Alta de nuevo producto
        # ------------------------------------------
        case "6":
            nombre_nuevo = input("Ingrese el nombre de la nueva herramienta: ").strip()

            if nombre_nuevo == "":
                print("Error: El nombre no puede estar vacío. Volviendo al menú principal.")
            elif nombre_nuevo in herramientas:
                print("Error: Esa herramienta ya existe en el catálogo. Volviendo al menú principal.")
            else:
                entrada_stock = input(f"Ingrese el stock inicial para '{nombre_nuevo}': ")
                if not entrada_stock.isdigit():
                    print("Error: El stock debe ser un número entero positivo o cero. Volviendo al menú principal.")
                elif int(entrada_stock) < 0:
                    print("Error: El stock no puede ser negativo. Volviendo al menú principal.")
                else:
                    herramientas.append(nombre_nuevo)
                    existencias.append(int(entrada_stock))
                    print(f"Herramienta '{nombre_nuevo}' agregada con {entrada_stock} unidades.")

        # ------------------------------------------
        # OPCIÓN 7: Actualización de stock
        # ------------------------------------------
        case "7":
            if len(herramientas) == 0:
                print("No hay herramientas cargadas.")
            else:
                nombre_op = input("Ingrese el nombre de la herramienta: ").strip()
                indice = -1
                for i in range(len(herramientas)):
                    if herramientas[i] == nombre_op:
                        indice = i

                if indice == -1:
                    print(f"La herramienta '{nombre_op}' no existe en el catálogo.")
                else:
                    print(f"\nHerramienta: {herramientas[indice]} | Stock actual: {existencias[indice]}")
                    print("  V - Venta (disminuir stock)")
                    print("  I - Ingreso (aumentar stock)")
                    tipo_op = input("Seleccione el tipo de operación (V/I): ").strip().upper()

                    match tipo_op:
                        case "V":
                            entrada_cantidad = input("Ingrese la cantidad a vender: ")
                            if entrada_cantidad.isdigit() and int(entrada_cantidad) > 0:
                                cantidad_venta = int(entrada_cantidad)
                                if cantidad_venta > existencias[indice]:
                                    print(f"Error: Stock insuficiente. Disponibles: {existencias[indice]} unidades.")
                                else:
                                    existencias[indice] -= cantidad_venta
                                    print(f"Venta registrada. Stock actualizado: {existencias[indice]} unidades.")
                            else:
                                print("Cantidad inválida. Debe ser un número entero positivo.")
                        case "I":
                            entrada_cantidad = input("Ingrese la cantidad a ingresar: ")
                            if entrada_cantidad.isdigit() and int(entrada_cantidad) > 0:
                                existencias[indice] += int(entrada_cantidad)
                                print(f"Ingreso registrado. Stock actualizado: {existencias[indice]} unidades.")
                            else:
                                print("Cantidad inválida. Debe ser un número entero positivo.")
                        case _:
                            print("Opción inválida. Debe ingresar V o I.")

        # ------------------------------------------
        # OPCIÓN 8: Salir
        # ------------------------------------------
        case "8":
            print("\nCerrando el sistema. ¡Hasta luego!")
            break

        # ------------------------------------------
        # OPCIÓN inválida
        # ------------------------------------------
        case _:
            print("Opción inválida. Ingrese un número del 1 al 8.")
