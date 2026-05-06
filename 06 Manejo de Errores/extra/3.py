class NumeroNegativo(Exception):
    pass

def NumeroNegativoError(numero):
    
    if numero < 0:
        raise NumeroNegativo("No puede ingresar un numero negativo")
    
while True:
    try:
        numero = input("Ingrese un numero")
        break
    
    except NumeroNegativo:
        NumeroNegativoError()

    except ValueError:
        print("Ingrese un numero!")

