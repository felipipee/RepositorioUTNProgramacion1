import math #importamos la libreria para usar la constante pi en el ejercicio 4

print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 1" + "/" * 10)
print("|" * 30)
print("*" * 30)

#Ejercicio 1
def saludo():
    print("Hola, mundo!")
saludo()

print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 2" + "/" * 10)
print("|" * 30)
print("*" * 30)

#Ejercicio 2
def saludo_personalizado(nombre):
    print(f"Hola, {nombre}!")
saludo_personalizado("Marcos")

print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 3" + "/" * 10)
print("|" * 30)
print("*" * 30)

#ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")
    print(f"Residencia: {residencia}")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")



informacion_personal(nombre, apellido, edad, residencia)
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 4" + "/" * 10)
print("|" * 30)
print("*" * 30)

#Ejercicio 4

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio = float(input("Ingrese el radio del círculo: "))
area_circulo = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area_circulo}")



def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

perimetro_circulo = calcular_perimetro_circulo(radio)
print(f"El perímetro del círculo con radio {radio} es: {perimetro_circulo}")

print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 5" + "/" * 10)
print("|" * 30)
print("*" * 30)