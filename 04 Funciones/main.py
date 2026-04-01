import math #importamos la libreria para usar la constante pi en el ejercicio 4
print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 1" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

#Ejercicio 1
def saludo():
    print("\tHola, mundo!")
saludo()

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 2" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

#Ejercicio 2
def saludo_personalizado(nombre):
    print(f"\tHola, {nombre}!")
saludo_personalizado("Marcos")

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 3" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

#ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"\tNombre: {nombre}")
    print(f"\tApellido: {apellido}")
    print(f"\tEdad: {edad}")
    print(f"\tResidencia: {residencia}")
    print(f"\tSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("\tIngrese su nombre: ")
apellido = input("\tIngrese su apellido: ")
edad = input("\tIngrese su edad: ")
residencia = input("\tIngrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 4" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

#Ejercicio 4

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio = float(input("\tIngrese el radio del círculo: "))
area_circulo = calcular_area_circulo(radio)
print(f"\tEl área del círculo con radio {radio} es: {area_circulo}")



def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

perimetro_circulo = calcular_perimetro_circulo(radio)
print(f"\tEl perímetro del círculo con radio {radio} es: {perimetro_circulo}")

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 5" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

#Ejercicio 5
def segundos_horas(segundos):
    horas = float(segundos / 3600)
    return horas

segundos = int(input("\tCuantos segundos deseas calcular? "))
horas = segundos_horas(segundos)
print(f"\tLas horas son: {horas:.2f}")

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 6" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

def tabla_multiplicar(numero):
    for i in range (1, 11):
     print(f"\t{numero} x {i} = {numero * i}")

numero = int(input("\tIngrese el numero para la tabla "))
tabla_multiplicar(numero)

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 7" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicación = a * b
    división = a / b
    mostrar = (f"\tLa suma da igual a {suma}", f"\tLa resta es igual a {resta}", f"\tLa multiplicación es igual a {multiplicación}", f"\tLa division es igual a {división}")
    for i in mostrar:
        print(i)
a = float(input("\tIngrese el primer número "))
b = float(input("\tIngrese el segundo número "))
operaciones_basicas(a, b)

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 8" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

def calcular_imc(peso, altura):
    cuadrado = altura * altura
    imc = peso / cuadrado
    print(f"\tTu imc es de {imc:.0f}")
peso = float(input("\tIngresa tu peso en kg: "))
altura = float(input("\tIngresa tu altura en metros: "))
calcular_imc(peso, altura)

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 9" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

def celsius_to_farenheight():
    celsius = float(input("\tIngrese la temperatura en grados Celsius: "))
    farenheight = (celsius * 9/5) + 32
    print(f"\tLa temperatura en grados Farenheight es: {farenheight:.2f}")
celsius_to_farenheight()

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "EJERCICIO 10" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"\tEl promedio de los números es: {promedio:.2f}")
    print()

a = float(input("\tIngrese el primer número: "))
b = float(input("\tIngrese el segundo número: "))
c = float(input("\tIngrese el tercer número: "))
calcular_promedio(a, b, c)

print()
print("*" * 30)
print("|" * 30)
print("/" * 10 + "FIN DEL TRABAJO PRACTICO" + "/" * 10)
print("|" * 30)
print("*" * 30)
print()