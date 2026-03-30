import random
# Importamos el módulo random para poder sortear números al azar

# ── LOOP PRINCIPAL DEL JUEGO ────────────────────────────────────────────────
# Este while True hace que el juego se repita hasta que el usuario diga que no quiere jugar más
while True:

    # ── INGRESO DEL CARTÓN ──────────────────────────────────────────────────
    numeros = []  # Lista vacía donde guardaremos los 25 números del usuario
    print("Ingresá 25 números únicos del 1 al 75 para tu cartón:")

    # Este while sigue pidiendo números hasta que el usuario haya ingresado 25
    while len(numeros) < 25:
        try:
            # int() convierte lo que escribe el usuario a número entero
            # Si el usuario escribe letras, int() falla y salta al except
            numero = int(input(f"Número {len(numeros) + 1}/25: "))

            if numero < 1 or numero > 75:
                # El número está fuera del rango permitido
                print("Número fuera de rango. Debe ser entre 1 y 75.")
            elif numero in numeros:
                # El número ya fue ingresado antes (no puede repetirse)
                print("Número duplicado. Ya lo ingresaste.")
            else:
                # El número es válido: lo agregamos a la lista
                numeros.append(numero)

        except ValueError:
            # Si el usuario escribió algo que no es número (ej: "abc"), caemos acá
            print("Ingresá un número válido.")

    # ── CONSTRUIR EL CARTÓN 5x5 ─────────────────────────────────────────────
    # Dividimos la lista de 25 números en 5 filas de 5 elementos cada una
    # i*5 es el inicio de cada fila, (i+1)*5 es el fin
    # Ejemplo: fila 0 → numeros[0:5], fila 1 → numeros[5:10], etc.
    carton = [numeros[i*5:(i+1)*5] for i in range(5)]

    print("\n" + "*" * 30)
    print("       ¡INICIA EL JUEGO!")
    print("*" * 30)

    # Mostramos el cartón antes de empezar
    print("\nTu cartón:")
    print("  B    I    N    G    O")  # Encabezado con las letras del BINGO
    for fila in carton:
        # :>2 alinea cada número a la derecha en un espacio de 2 caracteres
        print("  ".join(f"{n:>2}" for n in fila))
    print()

    # ── PREPARAR EL SORTEO ──────────────────────────────────────────────────
    sorteados = []               # Lista donde guardamos los números que van saliendo
    bolillas = list(range(1, 76))  # Lista con todos los números del 1 al 75
    random.shuffle(bolillas)     # Los mezclamos al azar (como revolver las bolillas)
    bingo = False                # Variable que indica si el usuario ganó o no

    # ── SORTEO UNO A UNO ────────────────────────────────────────────────────
    # Recorremos cada bolilla en el orden aleatorio que definió shuffle
    for bolilla in bolillas:
        sorteados.append(bolilla)  # La añadimos a la lista de sorteados

        # Avisamos si la bolilla está en el cartón del usuario
        en_carton = " ✔ ¡En tu cartón!" if bolilla in numeros else ""
        print(f"Número sorteado: {bolilla}{en_carton}")

        # ── VERIFICAR SI HAY BINGO ──────────────────────────────────────────

        # 1) Verificar FILAS: si todos los números de una fila fueron sorteados
        for fila in carton:
            if all(n in sorteados for n in fila):
                bingo = True
        # all() devuelve True solo si TODOS los elementos cumplen la condición

        # 2) Verificar COLUMNAS: si todos los números de una columna fueron sorteados
        # col va de 0 a 4 (cada columna), fila va de 0 a 4 (cada fila)
        for col in range(5):
            if all(carton[fila][col] in sorteados for fila in range(5)):
                bingo = True

        # 3) Verificar DIAGONAL PRINCIPAL (de arriba-izquierda a abajo-derecha)
        # Las posiciones son [0][0], [1][1], [2][2], [3][3], [4][4]
        if all(carton[i][i] in sorteados for i in range(5)):
            bingo = True

        # 4) Verificar DIAGONAL INVERSA (de arriba-derecha a abajo-izquierda)
        # Las posiciones son [0][4], [1][3], [2][2], [3][1], [4][0]
        if all(carton[i][4-i] in sorteados for i in range(5)):
            bingo = True

        # ── SI HAY BINGO, MOSTRAR CARTÓN Y TERMINAR ─────────────────────────
        if bingo:
            print("\nTu cartón:")
            print("  B    I    N    G    O")
            for fila in carton:
                fila_str = ""
                for n in fila:
                    # Si el número fue sorteado, mostramos * en su lugar
                    marcado = " *" if n in sorteados and n in numeros else f"{n:>2}"
                    fila_str += marcado + "  "
                print(fila_str)
            print("\n🎉 ¡BINGO! ¡Ganaste!")
            break  # Salimos del for de bolillas

    # Si se acabaron todas las bolillas y no hubo bingo
    if not bingo:
        print("Se acabaron las bolillas. ¡No hubo Bingo esta vez!")

    # ── PREGUNTAR SI QUIERE JUGAR DE NUEVO ──────────────────────────────────
    respuesta = input("\n¿Deseás jugar de nuevo? (s/n): ").lower()
    # .lower() convierte la respuesta a minúsculas para aceptar "S" o "s"

    # Si la respuesta no es ni "s" ni "n", seguimos preguntando
    while respuesta not in ("s", "n"):
        print("Ingresá 's' para sí o 'n' para no.")
        respuesta = input("¿Deseás jugar de nuevo? (s/n): ").lower()

    if respuesta == "n":
        print("¡Gracias por jugar! Hasta la próxima.")
        break  # Salimos del while True principal, terminando el programa
    # Si respondió "s", el while True vuelve a empezar desde arriba