energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

nombre_agente = input("Ingrese su nombre de agente: ")
while not nombre_agente.isalpha():
    print("Nombre no válido. Ingrese un nombre sin números ni símbolos.")
    nombre_agente = input("Ingrese su nombre de agente: ")

print(f"Bienvenido, Agente {nombre_agente}. Su misión: abrir las 3 cerraduras antes de quedarse sin energía o tiempo.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    # Verificar bloqueo por alarma
    if alarma and tiempo <= 3:
        print("Sistema bloqueado por alarma. ¡Has perdido!")
        break

    print(f"\n--- Estado: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'} ---")
    print("1. Forzar cerradura  (-20 energía, -2 tiempo)")
    print("2. Hackear panel     (-10 energía, -3 tiempo)")
    print("3. Descansar         (+15 energía, -1 tiempo)")

    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Opción no válida. Ingrese 1, 2 o 3.")
        opcion = input("Seleccione una opción: ")

    if opcion == "1":
        energia -= 20
        tiempo -= 2

        # Regla anti-spam: 3 veces seguidas forzando
        forzar_seguidas += 1
        if forzar_seguidas >= 3:
            print("¡La cerradura se trabó! Se activó la alarma automáticamente.")
            alarma = True
        else:
            # Riesgo de alarma si energía < 40
            if energia < 40:
                print("Energía baja. Hay riesgo de alarma.")
                numero_elegido = input("Ingrese un número del 1 al 3: ")
                while not numero_elegido.isdigit() or numero_elegido not in ["1", "2", "3"]:
                    print("Número no válido.")
                    numero_elegido = input("Ingrese un número del 1 al 3: ")
                if numero_elegido == "3":
                    print("Mala suerte... se activó la alarma.")
                    alarma = True
                else:
                    cerraduras_abiertas += 1
                    print(f"Cerradura forzada con éxito. Cerraduras abiertas: {cerraduras_abiertas}/3")
            else:
                cerraduras_abiertas += 1
                print(f"Cerradura forzada con éxito. Cerraduras abiertas: {cerraduras_abiertas}/3")

        print(f"Energía: {energia} | Tiempo: {tiempo}")

    elif opcion == "2":
        forzar_seguidas = 0  # Corta la racha
        energia -= 10
        tiempo -= 3

        for i in range(4):
            print(f"Hackeando{'.' * (i + 1)}")
            codigo_parcial += "A"

        print(f"Código parcial acumulado: {codigo_parcial} (longitud: {len(codigo_parcial)})")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"¡Código completo! Cerradura abierta automáticamente. Cerraduras: {cerraduras_abiertas}/3")

        print(f"Energía: {energia} | Tiempo: {tiempo}")

    elif opcion == "3":
        forzar_seguidas = 0  # Corta la racha
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1

        if alarma:
            energia -= 10
            print("La alarma está activa. Perdés 10 energía extra al descansar.")

        print(f"Descansaste. Energía: {energia} | Tiempo: {tiempo}")

    # Verificar bloqueo por alarma al final del turno
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nSistema bloqueado: alarma activa con poco tiempo. ¡DERROTA!")
        break

# Condiciones de fin
if cerraduras_abiertas == 3:
    print(f"\n¡VICTORIA! Agente {nombre_agente} abrió las 3 cerraduras y escapó.")
elif energia <= 0:
    print(f"\nDERROTA. Te quedaste sin energía.")
elif tiempo <= 0:
    print(f"\nDERROTA. Se acabó el tiempo.")
elif alarma:
    print(f"\nDERROTA por bloqueo de alarma.")
