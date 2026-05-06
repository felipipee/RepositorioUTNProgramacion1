while True:
    try:
        numero = int(input("Ingrese un numero entero "))
        print(f"Numero guardado {numero}")
        break
    except ValueError:
        print("Debe ingresar un numero entero")
        