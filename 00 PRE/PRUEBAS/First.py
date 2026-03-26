import calendar

mes_usuario = int(input("Ingrese un número de mes (1-12): "))
while mes_usuario < 1 or mes_usuario > 12:
    print("Número de mes inválido. Intente nuevamente.")
    mes_usuario = int(input("Ingrese un número de mes (1-12): "))
nombre_mes = calendar.month_name[mes_usuario]
print(f"El mes correspondiente al número {mes_usuario} es {nombre_mes}.")

if mes_usuario in 2:
    dias_mes = 28

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
