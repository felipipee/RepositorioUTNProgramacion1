continentes = ['America', 'Europa', 'Asia', 'Africa', 'Oceania']

class ErrorLetra(Exception):
    pass

def solo_letras(texto):
    if not texto.isalpha():
        raise ErrorLetra('Solo se permiten letras')

def mostrar_menu():
    print('''\n---Menu---
1. Agregar pais
2. Listar paises
3. Buscar pais
4. Modificar pais
5. Eliminar
6. Salir''')
    
def agregar_pais(paises):
    while True:
        try:
            while True:
                nombre = input('Ingrese el nombre del pais (Solo letras): ').capitalize().strip()
                if len(nombre) < 4:
                    print("Debe ingresar el nombre del pais")
                    continue
                solo_letras(nombre)
                break

            while True:
                poblacion = int(input('Ingrese la poblacion del pais(): '))
                if poblacion < 500:
                    print("Ingrese un numero de habitantes coherente")
                    continue
                break

            while True:
                superficie = float(input('Ingrese la superficie del pais: '))
                if superficie < 0.4:
                    print("La superficie debe ser igual o mayor a la del vaticano")
                    continue
                break

            while True:
                continente = input('Ingrese el continente del pais: ').capitalize().strip()
                solo_letras(continente)
                if continente not in continentes:
                    print("Ingrese un continente real")
                    continue
                break

        except ValueError:
            print("Ingrese lo que se pide ")
            continue
        except ErrorLetra as e:
            print(f'Error: {e}')
            continue

        else:
            pais_nvo = {
                'nombre': nombre,
                'poblacion': poblacion,
                'superficie': superficie,
                'continente' : continente
            }

            paises.append(pais_nvo)
            print('Pais agregado correctamente.')
            return paises



def listar_paises(paises):
    if not paises:
        print('No hay paises que mostrar.')
    else:
        for pais in paises:
            print()
            for k,v in pais.items():
                print(f'{k}: {v}')


def buscar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        try:
            nombre_pais = input('Ingrese el pais a buscar: ').capitalize().strip()
            solo_letras(nombre_pais)
        except ErrorLetra as e:
            print(f'Error: {e}')
            return

        encontrado = False
        for pais in paises:
            if nombre_pais == pais['nombre']:
                print(f'Pais encontrado: {pais}')
                encontrado = True
        if not encontrado:
            print('Pais no encontrado.')


def modificar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        try:
            nombre_pais = input('Ingrese el pais a modificar: ').capitalize().strip()
            solo_letras(nombre_pais)
        except ErrorLetra as e:
            print(f'Error: {e}')
            return paises

        encontrado = False
        for pais in paises:
            if nombre_pais == pais['nombre']:
                print(f'Pais encontrado: {pais}')
                encontrado = True

                while True:
                    try:
                        pais['poblacion'] = int(input(f'Ingrese la nueva poblacion para {pais["nombre"]}: '))
                        if pais['poblacion'] < 500:
                            print("Ingrese un numero de habitantes coherente")
                            continue
                        break
                    except ValueError:
                        print("Ingrese un numero valido")

                while True:
                    try:
                        pais['superficie'] = float(input(f'Ingrese la nueva superficie para {pais["nombre"]}: '))
                        if pais['superficie'] < 0.4:
                            print("La superficie debe ser igual o mayor a la del vaticano")
                            continue
                        break
                    except ValueError:
                        print("Ingrese un numero valido")

                print('Pais modificado')

        if not encontrado:
            print('Pais no encontrado.')
        
    return paises

def eliminar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        try:
            nombre_pais = input('Ingrese el pais a eliminar: ').capitalize().strip()
            solo_letras(nombre_pais)
        except ErrorLetra as e:
            print(f'Error: {e}')
        else:
            encontrado = False
            for pais in paises:
                if nombre_pais == pais['nombre']:
                    print(f'Pais encontrado')
                    encontrado = True
                    paises.remove(pais)
                    print('Pais eliminado.')
            if not encontrado:
                    print('Pais no encontrado.')
            return paises