notas = ()
alumnos = {}
alumnos_promedio = {}


cant_alumnos = input("Ingrese la cantidad de alumnos: , ingrese vacio para usar 3: ")

if cant_alumnos == "":
    cant_alumnos = '3'

while not cant_alumnos.isdigit():
    print("Error, ingrese solo numeros")
    cant_alumnos = input("Ingrese la cantidad de alumnos: , ingrese vacio para usar 3: ")
cant_alumnos = int(cant_alumnos)


for i in range(int(cant_alumnos)):
    
    alumno = input(f"Ingrese el nombre del alumno {i + 1}: ").capitalize()
    while not alumno.isalpha():
        print("Error, ingrese solo texto")
        alumno = input(f"Ingrese el nombre del alumno {i + 1}: ").capitalize()
    alumnos[alumno] = ()
    for i in range(3):
        
        nota = input(f"Ingrese la nota {i + 1} del alumno {alumno}: ")
        while not nota.isdigit():
            print("Error, ingrese solo numeros")
            nota = input(f"Ingrese la nota {i + 1} del alumno {alumno}: ")
        nota = int(nota)

        while nota <= 0 or nota > 10:
            print("Error, debe ser mayor a cero y menor o igual a 10")
            nota = input(f"Ingrese la nota {i + 1} del alumno {alumno}: ")

            while not nota.isdigit():
                print("Error, ingrese solo numeros")
                nota = input(f"Ingrese la nota {i + 1} del alumno {alumno}: ")
            nota = int(nota)
        


        alumnos[alumno] += (nota,)


for alumno in alumnos:
    promedio = sum(alumnos[alumno]) / len(alumnos[alumno])
    alumnos_promedio[alumno] = promedio

for alumno, promedio in alumnos_promedio.items():
    print(f"{alumno}: {promedio:.2f}")
