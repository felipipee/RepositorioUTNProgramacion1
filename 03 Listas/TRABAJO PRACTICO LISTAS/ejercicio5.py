#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada.

estudiantes = ["Ana", "Luis", "Marta", "Carlos", "Sofía", "Jorge", "Lucía", "Pedro"]
print("Lista de estudiantes:", estudiantes)
# Preguntar al usuario si quiere agregar o eliminar un estudiante
accion = input("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)? ").upper()
if accion == 'A':
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado.")
elif accion == 'E':
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print("Estudiante eliminado.")
    else:
        print("El estudiante no se encuentra en la lista.")
# Mostrar la lista final actualizada
print("Lista final de estudiantes:", estudiantes)