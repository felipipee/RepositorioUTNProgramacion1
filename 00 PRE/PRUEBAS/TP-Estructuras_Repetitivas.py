import random

#EJERCICIO 1
#Escribir un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for n in range (101):
    print (n)


#EJERCICIO 2
#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = input("Ingrese un número entero: ")
cantidad_digitos = len(num)
print("La cantidad de dígitos es:", cantidad_digitos)

#EJERCICIO 3
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer valor entero: "))
valor2 = int(input("Ingrese el segundo valor entero: "))

suma = 0
for n in range(valor1 + 1, valor2):
    suma += n
    print("La suma de los números entre", valor1, "y", valor2, "es:", suma)
    

#EJERCICIO 4
#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma_total = 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break
    suma_total += numero

print("El total acumulado es:", suma_total)

#EJERCICIO 5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        break

print(f"¡Adivinaste el número en", intentos, "intentos!")

#EJERCICIO 6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for y in range(100, -1, -1):
    if y % 2 == 0:
        print(y)

#EJERCICIO 7
#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario

num_positivo = int(input("Ingrese un número entero positivo: "))
suma_positivos = 0
for z in range(num_positivo + 1):
    suma_positivos += z
print("La suma de los números entre 0 y", num_positivo, "es:", suma_positivos)

#EJERCICIO 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad_numeros = 100
pares = 0
impares = 0
negativos = 0
positivos = 0
for _ in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)

#EJERCICIO 9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad_numeros_media = 100
suma_numeros = 0
for _ in range(cantidad_numeros_media):
    numero = int(input("Ingrese un número entero: "))
    suma_numeros += numero
media = suma_numeros / cantidad_numeros_media
print("La media de los números ingresados es:", media)

#EJERCICIO 10
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_invertir = input("Ingrese un número entero: ")
numero_invertido = numero_invertir[::-1]
print("El número invertido es:", numero_invertido)
