def mostrar_menu():
  print("""\n--- Menu ---
1. Agregar pais
2. Listar paises
3. Buscar pais
4. Modificar pais
5. Eliminar pais
6. Salir""")

# - - - - - #

def mostrar_paises(pais):
  indice = 0
  print()
  for k,v in pais.items():
    print(f"{indice + 1}: {k.capitalize()}: {v}")
    indice += 1

def mostrar_pais(pais):
  return f"{pais['nombre']} - Poblacion: {pais['poblacion']} - Superficie: {pais['superficie']} - Continente: {pais['continente']}"

# - - - - - #

def validar_texto(mensaje_1,mensaje_2 = None):
    while True:
      try:
        texto = input(mensaje_1).strip()
        if texto.isalpha():
          if mensaje_2 != None:
            print(mensaje_2)
          return texto
        else:
          print("ERROR... El texto solo puede contener letras.")
      except Exception as e:
        print(f"Hubo un error inesperado... Error: {e}.")
def validar_entero(mensaje_1,mensaje_2 = None):
  while True:
    try:
      numero = int(input(mensaje_1))
      if numero < 0:
        print("ERROR... No se permiten números negativos.")
        continue
      if mensaje_2 != None:
        print(mensaje_2)
      return numero
    except ValueError:
      print("ERROR... Por favor ingrese un número entero.")
    except Exception as e:
      print(f"Hubo un error inesperado... Error: {e}.")
def validar_flotante(mensaje_1,mensaje_2 = None):
  while True:
    try:
      numero = float(input(mensaje_1))
      if numero < 0:
        print("ERROR... No se permiten números negativos.")
        continue
      if mensaje_2 != None:
        print(mensaje_2)
      return numero
    except ValueError:
      print("ERROR... Por favor ingrese un número válido.")
    except Exception as e:
      print(f"Hubo un error inesperado... Error: {e}.")

# - - - - - #

def agregar_pais(paises):
  nombre = validar_texto("Ingrese el nombre del pais: ")
  if nombre in [pais["nombre"] for pais in paises]:
    print("El pais ya existe.")
  else:
    print("Nombre del pais ingresado correctamente.")
    poblacion = validar_entero("Ingrese la poblacion del pais: ", "Poblacion del pais ingresada correctamente.")
    superficie = validar_flotante("Ingrese la superficie del pais: ", "Superficie del pais ingresada correctamente.")
    continente = validar_texto("Ingrese el continente del pais: ", "Continente del pais ingresado correctamente.")
    paises.append({
      "nombre": nombre.capitalize(),
      "poblacion": poblacion,
      "superficie": superficie,
      "continente": continente.capitalize()
    })
    print("Pais agregado correctamente.")
  
  return paises

def listar_paises(paises):
  if not paises:
    print("No hay paises que mostrar.")
  else:
    print()
    for pais in paises:
      print(mostrar_pais(pais))

def buscar_pais(paises):
  if not paises:
    print("No hay paises cargados.")
  else:
    nombre_pais = validar_texto("Ingrese el pais a buscar: ")
    encontrado = False
    for pais in paises:
      if nombre_pais.capitalize() == pais["nombre"]:
        print(f"Pais encontrado: {mostrar_pais(pais)}")
        encontrado = True
    if not encontrado:
      print("Pais no encontrado.")

def modificar_pais(paises):
  if not paises:
    print("No hay paises cargados.")
  else:
    nombre_pais = validar_texto("Ingrese el pais a modificar: ")
    encontrado = False
    for pais in paises:
      if nombre_pais.capitalize() == pais["nombre"]:
        print(f"Pais encontrado: {mostrar_pais(pais)}")
        encontrado = True
        while True:
          opcion=input(f""" -- ELIJA UNA OPCIÓN --
1. Modificar población de {nombre_pais}
2. Modificar superficie de {nombre_pais}
3. Salir
- """)
          match opcion:
            case "1":
              pais['poblacion'] = validar_entero(f'Ingrese la nueva poblacion para {nombre_pais}: ', "Población modificada exitosamente.")
              break
            case "2":
              pais['superficie'] = validar_flotante(f'Ingrese la nueva superficie para {nombre_pais}: ', "Superficie modificada exitosamente.")
              break
            case "3":
              print("Volviendo al menú principal...")
              break
            case _:
              print("ERROR... Comando inválido")
    if not encontrado:
      print("Pais no encontrado.")
    return paises

def eliminar_pais(paises):
  if not paises:
    print("No hay paises cargados.")
  else:
    nombre_pais = validar_texto("Ingrese el pais a eliminar: ")
    encontrado = False
    for pais in paises:
      if nombre_pais.capitalize() == pais["nombre"]:
        print(f"Pais encontrado: {mostrar_pais(pais)}")
        encontrado = True
        paises.remove(pais)
        print("Pais eliminado")
    if not encontrado:
      print("Pais no encontrado.")
    return paises