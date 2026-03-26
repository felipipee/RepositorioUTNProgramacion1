#11) Dada una lista con los nombres de 10 estudiantes, pedir al usuario que ingrese un nombre y verificar si se encuentra en la lista.

nombres_estudiantes = ["Ana", "Luis", "Marta", "Carlos", "Sofía", "Jorge", "Lucía", "Pedro", "María", "Diego"]
nombre_a_buscar = input("Ingrese el nombre del estudiante a buscar: ")
if nombre_a_buscar in nombres_estudiantes:
    print(f"{nombre_a_buscar} se encuentra en la lista de estudiantes en la posición {nombres_estudiantes.index(nombre_a_buscar)}")
else:    
    print(f"{nombre_a_buscar} no se encuentra en la lista de estudiantes.")
