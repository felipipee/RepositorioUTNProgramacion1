import random
respuesta = input("¿Desea jugar de nuevo? (s/n): ").lower()

if respuesta == "s":
    print("¡Genial! Iniciando un nuevo juego...")
    numeros = []
    carton = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(25):
        numero = int(input("Ingrese un número del 1 al 75: "))
        while numero < 1 or numero > 75 or numero in numeros or not numero.isdigit():
            print("Número inválido. Por favor, ingrese un número del 1 al 75 que no haya sido ingresado anteriormente.")
            numero = int(input("Ingrese un número del 1 al 75: "))
        numeros.append(numero)
    
    # Llenar el cartón con los números ingresados
    #Como el cartón es de 5x5, se necesitan 25 números para llenarlo. Se asignan los números ingresados al cartón en orden, llenando cada fila de izquierda a derecha.
    #con dos bucles anidados, el bucle externo itera sobre las filas del cartón (de 0 a 4) y el bucle interno itera sobre las columnas (de 0 a 4). En cada iteración, se asigna el número correspondiente de la lista "numeros" al cartón en la posición [i][j], donde i es el índice de la fila y j es el índice de la columna. El número asignado se calcula como i * 5 + j, lo que garantiza que se llenen las filas de izquierda a derecha con los números ingresados.
    for i in range(5):
        for j in range(5):
            carton[i][j] = numeros[i * 5 + j]
    
    print("*" * 30)
    print("|" * 30)
    print("/" * 10 + "INICIA EL JUEGO!" + "/" * 10)
    print("|" * 30)
    print("*" * 30)
    
    #imprimir el cartón de bingo
    print("Cartón de Bingo:")
    for fila in carton:
        print(fila)
    
    numeros_sorteados = []
    while len(numeros_sorteados) < 75:
        numero_sorteado = random.randint(1, 75)
        if numero_sorteado not in numeros_sorteados:
            numeros_sorteados.append(numero_sorteado)
            print(f"Número sorteado: {numero_sorteado}")
        elif numero_sorteado in numeros:
                print(f"¡Número en el cartón! {numero_sorteado} Sigue jugando.")
        elif all(num in numeros_sorteados for num in numeros):
            print("¡Bingo! Has ganado el juego. ¿Desea jugar de nuevo? (s/n)")
            respuesta = input().lower()
            break
        elif respuesta == "n":
            print("¡Gracias por jugar! Hasta la próxima.")
        else:
            print("Respuesta no válida. Por favor, ingrese 's' para sí o 'n' para no.")

