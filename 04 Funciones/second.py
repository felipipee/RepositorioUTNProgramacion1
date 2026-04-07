import random
lista_palabras = ["Lionel", "Antonela", "Thiago", "Mateo", "Ciro", "Santino", "Benicio", "Francisco", "Joaquin", "Valentino", "Bautista", "Agustin", "Lihuel", "Federico", "Bruno", "Manuel", "Santiago", "Luca", "Matias", "Nicolas", "Emiliano", "Federico", "Gonzalo", "Agustin", "Federico", "Bruno", "Manuel", "Santiago", "Luca", "Matias", "Nicolas", "Emiliano", "Diegote", "Adolfo", "Austria"]



def jugar_ahorcado():
    print("Bienvenido al ahorcado")
    jugar = input("Quiere jugar?: ")
    while jugar not in ("s", "n"):
        print("Opción inválida")
        jugar = input("Jugar? (s/n): ")

    if jugar == "n":
        print("Gracias por jugar, vuelva pronto")
        return

    while jugar == "s":
        print("Comenzando el juego")
        randomizado = random.choice(lista_palabras)
        letras_adivinadas = ["_"] * len(randomizado)
        intentos = 0

        while True:
            print("-" * len(randomizado))
            input_usuario = input("Ingrese una letra: ")

            if input_usuario == randomizado:
                print("¡Ganaste! La palabra era:", randomizado)
                break

            if input_usuario in randomizado:
                print("Letra correcta")
            else:
                intentos += 1
                print("Letra incorrecta. Intentos:", intentos)
            if intentos >= 6:
                print("¡Perdiste! La palabra era:", randomizado)
                break

        jugar = input("Quiere jugar otra vez? (s/n): ")
        while jugar not in ("s", "n"):
            print("Opción inválida")
            jugar = input("Jugar? (s/n): ")

jugar_ahorcado()