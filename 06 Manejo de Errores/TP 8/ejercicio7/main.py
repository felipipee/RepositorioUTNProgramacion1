while True:
    try:
        entrada = input("Ingrese un numero: ")
        
        # Intentamos convertir a entero. 
        # Si el usuario ingresa letras, Python salta directo al except ValueError.
        numero = int(entrada)
        
        print(f"Numero ingresado correctamente como {numero}")
        break # Si todo salió bien, cortamos el bucle

    except ValueError:
        # Aquí manejamos específicamente cuando el valor no es numérico
        print("Debe ingresar un número válido")

    except Exception as error:
        # Cualquier otro error que no hayamos previsto
        print(f"Se produjo un error inesperado || {error}")