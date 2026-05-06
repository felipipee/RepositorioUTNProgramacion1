from funciones import *


habitaciones = []

while True:
    try:
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            agregar_habitacion(habitaciones)
        elif opcion == '2':
            mostrar_habitaciones(habitaciones)
        elif opcion == '3':
            consultar_habitacion(habitaciones)
        elif opcion == '4':
            cambiar_estado(habitaciones)
        elif opcion == '5':
            listar_por_estado(habitaciones)
        elif opcion == '6':
            print('Hasta luego!')
            break
        else:
            print('Opción inválida.')

    except ErrorHotel as e:
        print(f'Error del hotel: {e}')