contactos = {'Juan': 12345678, 'María': 87654321, 'Pedro': 11223344, 'Ana': 44332211, 'Luis': 55667788}

ingresar_contactos = input("¿Desea ingresar un nuevo contacto? (s/n): ").lower()
while ingresar_contactos != 's' and ingresar_contactos != 'n':
    print("Error, ingrese solo 's' o 'n'")
    ingresar_contactos = input("¿Desea ingresar un nuevo contacto? (s/n): ").lower()
if ingresar_contactos == 's':
    nombre = input("Ingrese el nombre del contacto: ").capitalize()
    while not nombre.isalpha():
        print("Error, ingrese solo texto")
        nombre = input("Ingrese el nombre del contacto: ").capitalize()
    numero = input("Ingrese el número del contacto: ")
    while not numero.isdigit():
        print("Error, ingrese solo números")
        numero = input("Ingrese el número del contacto: ")
    numero = int(numero)
    contactos[nombre] = numero
    ingresar_contactos = input("¿Desea ingresar otro contacto? (s/n): ").lower()
    while ingresar_contactos != 's' and ingresar_contactos != 'n':
        print("Error, ingrese solo 's' o 'n'")
        ingresar_contactos = input("¿Desea ingresar otro contacto? (s/n): ").lower()
else:
    print("No se han ingresado nuevos contactos.")

def mostrar_consulta(nombre):
    if nombre in contactos:
        print(f"El número de {nombre} es: {contactos[nombre]}")
    else:
        print(f"{nombre} no se encuentra en la lista de contactos.")


nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ").capitalize()
while not nombre_consulta.isalpha():
    print("Error, ingrese solo texto")
    nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ").capitalize()
mostrar_consulta(nombre_consulta)