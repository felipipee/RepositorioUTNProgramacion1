#TypeError, ya que no se puede dividir un int con un string, esto se arregla convirtiendo el input a entero, y validando antes de convertir
try:
    a = 10
    b = input("Introduce un número: ")

    result = a / b
    print(f"Resultado: {result}")
except TypeError:
    print("Error, no se puede dividir un numero con un string")

#En el caso de que estuviera el input convertido a un entero y el usuario ingresara un 0 se usaria esta excepcion
except ZeroDivisionError:
    print("No se puede dividir un numero por 0")

#IndexError, ya que busca un elemento con un index mayor a los disponibles, 0-2
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Buscando un elemento que no existe")




