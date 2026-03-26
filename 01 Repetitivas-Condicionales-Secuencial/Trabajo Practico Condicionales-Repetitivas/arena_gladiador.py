nombre_gladiador = input("--- BIENVENIDO A LA ARENA ---\nNombre del Gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"\n{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

    if opcion == "1":
        # Golpe crítico si enemigo tiene menos de 20 HP
        if vida_enemigo < 20:
            danio_final = float(danio_base * 1.5)
            print(f"¡GOLPE CRÍTICO! Atacaste al enemigo por {danio_final} puntos de daño.")
        else:
            danio_final = float(danio_base)
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")
        vida_enemigo -= int(danio_final)

    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == "3":
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print(f"Usaste una poción. HP: {vida_gladiador} | Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")

    # Turno del enemigo (siempre ataca después de tu acción)
    if vida_enemigo > 0:
        vida_gladiador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

    if vida_gladiador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

# Fin del juego
if vida_gladiador > 0:
    print(f"\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")
