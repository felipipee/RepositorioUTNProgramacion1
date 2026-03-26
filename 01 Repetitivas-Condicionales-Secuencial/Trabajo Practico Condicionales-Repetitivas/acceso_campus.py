usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso_concedido = False

while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido. ¡Bienvenido al campus virtual!")
        acceso_concedido = True
        break
    else:
        intentos += 1
        print("Error: credenciales inválidas.")
else:
    print("Cuenta bloqueada. Ha excedido el número máximo de intentos.")

if acceso_concedido:
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")

        opcion = input("Opción: ")
        while not opcion.isdigit() or opcion not in ["1", "2", "3", "4"]:
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

        if opcion == "1":
            print("Estado de inscripción: Inscripto")
        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")
            confirmacion_clave = input("Confirme su nueva clave: ")
            if nueva_clave == confirmacion_clave:
                clave_correcta = nueva_clave
                print("Clave cambiada exitosamente.")
            else:
                print("Las claves no coinciden. Intente nuevamente.")
        elif opcion == "3":
            print("¡Tú puedes lograrlo! ¡Sigue adelante!")
        elif opcion == "4":
            print("Saliendo del campus virtual. ¡Hasta luego!")
            break
