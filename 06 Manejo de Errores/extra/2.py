while True:
    try:
        num1 = input("Ingrese el primer numero ")
        num2 = input("Ingrese el segundo numero")

        division  = num1 / num2

        print(f"Division: {division}")

    except ValueError:
        print("Debe ingresar numeros")

    except ZeroDivisionError:
        print("No se puede dividir por cero!")