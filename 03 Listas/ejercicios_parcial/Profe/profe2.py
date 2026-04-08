nombres = []
edades = []
notas = []
while True:
    print(f"\n Opciones")
    print("1. Cargar alumnos (nombres, edades, notas) ")
    print("2. Eliminar alumno")
    print("3. Mostrar a los alumnos")
    print("4. Cerrar programa")
    option = input("Ingrese la opción a cargar: ").strip()
    while not option.isalpha:
        print("Opción inaceptable")
        option = input("Ingrese la opción a cargar")
    match(option):
        case "1":
            alumnos_cargar = input("Cuanntos alumnos desea cargar (número): ")
            while not alumnos_cargar.strip().isdigit():
                print("Ingrese un número")
                alumnos_cargar = input("Cuanntos alumnos desea cargar (número): ")
            alumnos_cargar = int(alumnos_cargar)
            
            for i in range(alumnos_cargar):
                print("Ingrese el nombre del alumno")
                nombre = input("Nombre del alumno: ").capitalize()
                while not nombre.strip().isalpha():
                    print("error, solo se pueden ingresar letras")
                    nombre = input("Nombre del alumno: ").capitalize()
                print(f"Alumno ingresado como {nombre}")
                nombres.append(nombre)
                print("Ingrese la edad del alumno")
                edad = (input(f"Ingrese la edad de {nombre}: "))
                while not edad.strip().isdigit():
                    print("Ingrese un número")
                    edad = (input(f"Ingrese la edad de {nombre}: "))
                if edad.isdigit:
                    print(f"Edad de {nombre}, ingresada como {edad}")
                    edades.append(edad)
                print("Ingrese la nota del alumno")
                
                nota = input(f"Ingrese la nota de {nombre} (1-10): ").strip()
                while not nota.isdigit() or int(nota) < 1 or int(nota) > 10:
                    print("Error: ingresá un número del 1 al 10")
                    nota = input(f"Ingrese la nota de {nombre} (1-10): ").strip()
                nota = int(nota)
                notas.append(nota)
            pass
        case "2":
            alumno_eliminar = input("Nombre del alumno: ").capitalize()
            while not alumno_eliminar.strip().isalpha():
                    print("error, solo se pueden ingresar letras")
                    alumno_eliminar = input("Nombre del alumno: ").capitalize()
            while not alumno_eliminar in nombres:
                print("alumno no encontrado en la base de datos")
                alumno_eliminar = input("Nombre del alumno: ").capitalize()
            if alumno_eliminar in nombres:
                indice = nombres.index(alumno_eliminar)
                nombres.pop(indice)
                edades.pop(indice)
                notas.pop(indice)
            pass
        case "3":
            print("Mostrar alumnos (nombres, edades, notas)")
            print(f"{nombres}")
            print(f"{edades}")
            print(f"{notas}")
            pass
        case "4":
            print("Cerrando el programa")
            break
        case _:
            print("Opción inválida, intente de nuevo")
            pass