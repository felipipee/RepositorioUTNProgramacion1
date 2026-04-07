alumnos = []
notas = []

while True: 
    print(f"\n Bienvenido al sistema")
    print("Opciones")
    print("")
    print("1. Agregar alumno")
    print("2. Eliminar alumno")
    print("3. Ver nota de un alumno")
    print("4. Modificar nota")
    print("5. Alumnos desaprobados")
    print("6. Promedio del curso")
    print("7- Listado completo")
    print("8. Salir")

    opcion = input("Ingrese la opción a procesar: ")
    match opcion:

        case '1':
            print("Agregar alumno")
            Nombre = input("Ingrese el nombre del alumno").capitalize()
            while not Nombre.isalpha():
                Nombre = input("Ingrese el nombre del alumno").capitalize()
            alumnos.append(Nombre)
            print(f"Alumno ingresado como {Nombre}")
            Nota = input("Ingrese la nota del alumno (1-10): ")
            while not Nota.isdigit():
                print("Inválido, ingrese un numero del 1-10")
                Nota = input("Ingrese la nota del alumno (1-10): ")
            notas.append(Nota)
            pass
        case '2':
            print("Eliminar alumno")
            alumno_eliminar = input("Ingrese el nombre del alumno a eliminar: ").capitalize()
            while not alumno_eliminar.isalpha():
                print("Invalido")
                alumno_eliminar = input("Ingrese el nombre del alumno a eliminar: ").capitalize()
            notas.pop(alumnos.index(alumno_eliminar))
            alumnos.pop(alumnos.index(alumno_eliminar))
            
            pass
        case '3':
            print("Ver nota de alumno")
            alumno_nota = input("Ingrese el nombre del alumno para ver la nota: ").capitalize()
            while not alumno_nota.isalpha():
                print("Invalido")
                alumno_nota = input("Ingrese el nombre del alumno a eliminar: ").capitalize()
            indice = alumnos.index(alumno_nota)
            print(f"Nota del alumno {alumno_nota}: {notas[indice]}")
            pass
        case '4':
            print("Modificar nota de un alumno")
            alumno_edit = input("Ingrese el nombre del alumno: ").capitalize()        
            while not alumno_edit.isalpha():
                print("Invalido")
                alumno_edit = input("Ingrese el nombre del alumno: ").capitalize()  
            indice = alumnos.index(alumno_edit)
            print(f"Nota actual de: {alumno_edit} {notas[indice]}")
            nota_new = input("Ingrese la nota nueva: ")

            notas.insert(indice, nota_new)
            notas.remove(notas[indice + 1])
            
            
            pass
        case '5':
            for i in notas:
                if notas(i) < 7:
                    indice = notas.index()
                    print(f"Alumno {alumnos(indice)}, Nota: {notas(indice)}")
            pass
        case '6':
            numero = len(notas)
            cantidad = sum(notas)
            promedio_notas = cantidad / numero
            print(f"Promedio de notas: {promedio_notas}")
            pass
        case '7':
            print(alumnos)
            print(notas)
            pass
        case '8':
            print("Saliendo del programa")
            break

        case _:
            print("Opcion inv ")
            pass