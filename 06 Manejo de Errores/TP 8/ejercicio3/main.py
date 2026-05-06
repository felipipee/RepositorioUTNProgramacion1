#TypeError, ya que no se puede dividir un int con un string, esto se arregla convirtiendo el input a entero, y validando antes de convertir
try:
    a = 10
    b = input("Introduce un número: ")

    result = a / b
    print(f"Resultado: {result}")
except TypeError:
    print("Error, no se puede dividir un numero con un string")

#IndexError, ya que busca un elemento con un index mayor a los disponibles, 0-2
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Buscando un elemento que no existe")




