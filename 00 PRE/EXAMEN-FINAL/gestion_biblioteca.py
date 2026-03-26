# Sistema de Gestión de Biblioteca Escolar
# Examen Final - Pre ingreso TUP-FRM

# Listas paralelas para almacenar títulos y ejemplares
titulos = []
ejemplares = []

# Variable para controlar el bucle principal
continuar = True

print("=" * 60)
print("SISTEMA DE GESTIÓN DE BIBLIOTECA ESCOLAR")
print("=" * 60)

# Bucle principal del programa
while continuar:
    print("\n" + "=" * 60)
    print("MENÚ PRINCIPAL")
    print("=" * 60)
    print("1. Ingresar títulos")
    print("2. Mostrar catálogo")
    print("3. Consultar disponibilidad")
    print("4. Listar agotados")
    print("5. Agregar título")
    print("6. Actualizar ejemplares (préstamo/devolución)")
    print("7. Salir")
    print("=" * 60)
    
    opcion = input("Seleccione una opción (1-7): ")
    
    # Menú con estructura condicional
    if opcion == "1":
        # Opción 1: Ingresar títulos iniciales
        print("\n--- INGRESAR TÍTULOS INICIALES ---")
        
        cantidad_titulos = input("¿Cuántos títulos desea ingresar?: ")
        
        # Validar que sea un número entero positivo
        if cantidad_titulos.isdigit() and int(cantidad_titulos) > 0:
            cantidad_titulos = int(cantidad_titulos)
            
            i = 0
            while i < cantidad_titulos:
                print(f"\nTítulo {i + 1} de {cantidad_titulos}")
                titulo = input("Ingrese el título del libro: ").strip()
                
                # Validar que el título no esté vacío
                if titulo == "":
                    print("ERROR: El título no puede estar vacío.")
                    continue
                
                # Verificar que el título no esté duplicado
                titulo_existe = False
                j = 0
                while j < len(titulos):
                    if titulos[j].lower() == titulo.lower():
                        titulo_existe = True
                        break
                    j = j + 1
                
                if titulo_existe:
                    print(f"ERROR: El título '{titulo}' ya existe en el catálogo.")
                    continue
                
                # Ingresar cantidad de ejemplares
                cantidad_ejemplares = input("Ingrese la cantidad de ejemplares: ")
                
                # Validar que sea un número entero no negativo
                if cantidad_ejemplares.isdigit():
                    cantidad_ejemplares = int(cantidad_ejemplares)
                    
                    # Agregar a las listas paralelas
                    titulos.append(titulo)
                    ejemplares.append(cantidad_ejemplares)
                    
                    print(f"✓ Título '{titulo}' agregado con {cantidad_ejemplares} ejemplares.")
                    i = i + 1
                else:
                    print("ERROR: La cantidad de ejemplares debe ser un número entero no negativo.")
        else:
            print("ERROR: Debe ingresar un número entero positivo.")
    
    elif opcion == "2":
        # Opción 2: Mostrar catálogo
        print("\n--- CATÁLOGO COMPLETO ---")
        
        if len(titulos) == 0:
            print("El catálogo está vacío. No hay libros registrados.")
        else:
            print(f"\nTotal de títulos en catálogo: {len(titulos)}\n")
            print("-" * 60)
            i = 0
            while i < len(titulos):
                print(f"{i + 1}. {titulos[i]}")
                print(f"   Ejemplares disponibles: {ejemplares[i]}")
                print("-" * 60)
                i = i + 1
    
    elif opcion == "3":
        # Opción 3: Consultar disponibilidad
        print("\n--- CONSULTAR DISPONIBILIDAD ---")
        
        if len(titulos) == 0:
            print("El catálogo está vacío. No hay libros para consultar.")
        else:
            titulo_buscar = input("Ingrese el título a buscar: ").strip()
            
            if titulo_buscar == "":
                print("ERROR: El título no puede estar vacío.")
            else:
                # Buscar el título en la lista
                encontrado = False
                i = 0
                while i < len(titulos):
                    if titulos[i].lower() == titulo_buscar.lower():
                        print(f"\nTítulo: {titulos[i]}")
                        print(f"Ejemplares disponibles: {ejemplares[i]}")
                        encontrado = True
                        break
                    i = i + 1
                
                if not encontrado:
                    print(f"El título '{titulo_buscar}' no existe en el catálogo.")
    
    elif opcion == "4":
        # Opción 4: Listar agotados
        print("\n--- TÍTULOS AGOTADOS ---")
        
        if len(titulos) == 0:
            print("El catálogo está vacío.")
        else:
            # Buscar títulos con 0 ejemplares
            hay_agotados = False
            i = 0
            while i < len(titulos):
                if ejemplares[i] == 0:
                    if not hay_agotados:
                        print("\nLos siguientes títulos están agotados:\n")
                        print("-" * 60)
                        hay_agotados = True
                    print(f"• {titulos[i]}")
                i = i + 1
            
            if not hay_agotados:
                print("\n¡Excelente! No hay títulos agotados en este momento.")
            else:
                print("-" * 60)
    
    elif opcion == "5":
        # Opción 5: Agregar título
        print("\n--- AGREGAR NUEVO TÍTULO ---")
        
        titulo_nuevo = input("Ingrese el título del libro: ").strip()
        
        # Validar que el título no esté vacío
        if titulo_nuevo == "":
            print("ERROR: El título no puede estar vacío.")
        else:
            # Verificar que el título no esté duplicado
            titulo_existe = False
            i = 0
            while i < len(titulos):
                if titulos[i].lower() == titulo_nuevo.lower():
                    titulo_existe = True
                    break
                i = i + 1
            
            if titulo_existe:
                print(f"ERROR: El título '{titulo_nuevo}' ya existe en el catálogo.")
            else:
                # Ingresar cantidad de ejemplares
                cantidad_ejemplares = input("Ingrese la cantidad de ejemplares: ")
                
                # Validar que sea un número entero no negativo
                if cantidad_ejemplares.isdigit():
                    cantidad_ejemplares = int(cantidad_ejemplares)
                    
                    # Agregar a las listas paralelas
                    titulos.append(titulo_nuevo)
                    ejemplares.append(cantidad_ejemplares)
                    
                    print(f"✓ Título '{titulo_nuevo}' agregado exitosamente con {cantidad_ejemplares} ejemplares.")
                else:
                    print("ERROR: La cantidad de ejemplares debe ser un número entero no negativo.")
    
    elif opcion == "6":
        # Opción 6: Actualizar ejemplares (préstamo/devolución)
        print("\n--- ACTUALIZAR EJEMPLARES ---")
        
        if len(titulos) == 0:
            print("El catálogo está vacío. No hay libros disponibles.")
        else:
            titulo_actualizar = input("Ingrese el título del libro: ").strip()
            
            if titulo_actualizar == "":
                print("ERROR: El título no puede estar vacío.")
            else:
                # Buscar el título en la lista
                encontrado = False
                indice = 0
                i = 0
                while i < len(titulos):
                    if titulos[i].lower() == titulo_actualizar.lower():
                        encontrado = True
                        indice = i
                        break
                    i = i + 1
                
                if not encontrado:
                    print(f"ERROR: El título '{titulo_actualizar}' no existe en el catálogo.")
                else:
                    print(f"\nTítulo: {titulos[indice]}")
                    print(f"Ejemplares actuales: {ejemplares[indice]}")
                    print("\nSeleccione la operación:")
                    print("1. Préstamo (disminuir ejemplares)")
                    print("2. Devolución (aumentar ejemplares)")
                    
                    operacion = input("Opción (1-2): ")
                    
                    if operacion == "1":
                        # Préstamo
                        if ejemplares[indice] > 0:
                            ejemplares[indice] = ejemplares[indice] - 1
                            print(f"✓ Préstamo registrado. Ejemplares restantes: {ejemplares[indice]}")
                        else:
                            print("ERROR: No hay ejemplares disponibles para préstamo.")
                    
                    elif operacion == "2":
                        # Devolución
                        ejemplares[indice] = ejemplares[indice] + 1
                        print(f"✓ Devolución registrada. Ejemplares actuales: {ejemplares[indice]}")
                    
                    else:
                        print("ERROR: Opción inválida. Debe seleccionar 1 o 2.")
    
    elif opcion == "7":
        # Opción 7: Salir
        print("\n" + "=" * 60)
        print("Gracias por usar el Sistema de Gestión de Biblioteca")
        print("¡Hasta pronto!")
        print("=" * 60)
        continuar = False
    
    else:
        # Opción inválida
        print("\nERROR: Opción inválida. Por favor seleccione un número entre 1 y 7.")

# Fin del programa
