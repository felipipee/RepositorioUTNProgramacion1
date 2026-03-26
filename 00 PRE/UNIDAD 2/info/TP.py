from statistics import mean, median, mode
import random
import calendar


print("-" * 40)
# EJERCICIO 1

edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario >= 18:
    print("Eres mayor de edad.")
print("-" * 40)
# EJERCICIO 2

nota_usuario = int(input("Ingrese su nota (0-10): "))
if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# EJERCICIO 3
print("-" * 40)

numero_usuario = int(input("Ingrese un número: "))
while numero_usuario % 2 != 0:
    print("El número es impar. Intente nuevamente.")
    numero_usuario = int(input("Ingrese un número: "))
print("Ingresaste un número par.")

print("-" * 40)
# EJERCICIO 4

edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario < 12:
    print("Niño/a")   
elif 12 <= edad_usuario < 18:
    print("Adolescente")
elif 10 <= edad_usuario < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


print("-" * 40)
# EJERCICIO 5

contraseña_usuario = input("Ingrese la contraseña: ")
length_contraseña = len(contraseña_usuario)

while length_contraseña <= 7 or length_contraseña >= 15:
    print("Contraseña inválida. Debe tener entre 8 y 14 caracteres.")
    contraseña_usuario = input("Ingrese la contraseña nuevamente: ")
    length_contraseña = len(contraseña_usuario)

print("Contraseña válida")
print("-" * 40)

# EJERCICIO 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

print("Números aleatorios generados:")
print(numeros_aleatorios)

mediana_numeros = median(numeros_aleatorios)
media_numeros = mean(numeros_aleatorios)
moda_numeros = mode(numeros_aleatorios)

if media_numeros > mediana_numeros and media_numeros > moda_numeros:
    resultado = "Sesgo positivo"
elif media_numeros < mediana_numeros and media_numeros < moda_numeros:
    resultado = "Sesgo negativo"
else:
    resultado = "Distribución simétrica"

print("-" * 40)
print("El sesgo es:")
print(resultado)
print("-" * 40)

# EJERCICIO 7
vocales = "aeiouAEIOU"
frase = input("Ingrese una frase:")
ultima_letra = frase[-1]
vocales = "aeiouAEIOU"
frase = input("Ingrese una frase:")
ultima_letra = frase[-1]
if ultima_letra in vocales:
    frase = frase + "!"
    print("La frase termina con una vocal.")    
    print(frase)
else:
    print("La frase termina con una consonante.")    
    print(frase)

print("-" * 40)
# EJERCICIO 8
nombre_usuario = input("Ingrese su nombre de usuario: ")
print("Elija una opcion: 1. En mayusculas /n 2. En minusculas /n 3. Capitalizar")
opcion = int(input("Ingrese la opcion deseada (1, 2 o 3): "))
if opcion == 1:
    resultado = nombre_usuario.upper()  
    print(resultado)
elif opcion == 2:
    resultado = nombre_usuario.lower()
    print(resultado)
elif opcion == 3:   
    resultado = nombre_usuario.capitalize()
    print(resultado)
else:
    resultado = "Opcion invalida."
    print(resultado)


print("-" * 40)
# EJERCICIO 9

print("Ingrese la magnitud del temblor")
magnitud = float(input("Magnitud: "))
if magnitud < 3.0:
    print("Muy leve")
elif 3.0 <= magnitud < 4.0:
    print("Leve")
elif 4.0 <= magnitud < 5.0:
    print("Moderado")
elif 5.0 <= magnitud < 6.0:
    print("Fuerte")
elif 6.0 <= magnitud < 7.0:
    print("Muy fuerte")
elif 7.0 <= magnitud:
    print("Extremo")

print("-" * 40)

# EJERCICIO 10

mes_usuario = int(input("Ingrese un número de mes (1-12): "))
while mes_usuario < 1 or mes_usuario > 12:
    print("Número de mes inválido. Intente nuevamente.")
    mes_usuario = int(input("Ingrese un número de mes (1-12): "))
nombre_mes = calendar.month_name[mes_usuario]
print(f"El mes correspondiente al número {mes_usuario} es {nombre_mes}.")

dia_usuario = int(input("Ingrese un número de día (1-31): "))
while dia_usuario < 1 or dia_usuario > 31:
    print("Número de día inválido. Intente nuevamente.")
    dia_usuario = int(input("Ingrese un número de día (1-31): "))   
print(f"El día ingresado es: {dia_usuario}.")


hemisferio_usuario = input("Ingrese su hemisferio (Norte/Sur): ").strip().lower()
while hemisferio_usuario not in ["norte", "sur"]:
    print("Hemisferio inválido. Intente nuevamente.")
    hemisferio_usuario = input("Ingrese su hemisferio (Norte/Sur): ").strip().lower()

if hemisferio_usuario == "norte":
    if (mes_usuario in [12, 1, 2]) or (mes_usuario == 3 and dia_usuario < 21):
        resultado = "Invierno"
    elif (mes_usuario in [3, 4, 5]) or (mes_usuario == 6 and dia_usuario < 21):
        resultado = "Primavera"
    elif (mes_usuario in [6, 7, 8]) or (mes_usuario == 9 and dia_usuario < 23):
        resultado = "Verano"
    else:
        resultado = "Otoño"
else:
    if (mes_usuario in [6, 7, 8]) or (mes_usuario == 9 and dia_usuario < 23):
        resultado = "Invierno"
    elif (mes_usuario in [9, 10, 11]) or (mes_usuario == 12 and dia_usuario < 21):
        resultado = "Primavera"
    elif (mes_usuario in [12, 1, 2]) or (mes_usuario == 3 and dia_usuario < 21):
        resultado = "Verano"
    else:
        resultado = "Otoño"

print(f"La estación es: {resultado}.")











