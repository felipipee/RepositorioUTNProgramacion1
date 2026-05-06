from fcs import menu as m
from fcs import caso1 as c1
from fcs import caso2 as c2
from fcs import caso3 as c3
from fcs import caso4 as c4
from fcs import caso5 as c5
habitaciones = []

while True:

    m()
    try:
        opcion = int(input("Ingrese la opción que desee procesar "))
    except ValueError:
        print("Opción no válida, por favor ingrese un número")
        continue

    match opcion:
        case 1:
            c1(habitaciones)
        case 2:
            c2(habitaciones)
            
        case 3:
            c3(habitaciones)
            
            
        case 4:
            c4(habitaciones)
            
            
        case 5:
            c5(habitaciones)
            
        case 6:
            print("Saliendo del programa")
            break
        case _:
            print("Opción desconocida")