
a = 10
b = input("Introduce un número: ")

result = a / b
#TypeError, ya que no se puede dividir un int con un string, esto se arregla convirtiendo el input a entero, y validando antes de convertir

print(f"Resultado: {result}")
numbers = [1, 2, 3]
print(numbers[5])

#IndexError, ya que busca un elemento con un index mayor a los disponibles, 0-2

