from excepciones_hotel import *
 
 
def mostrar_menu():
    print('\n1. Agregar habitación')
    print('2. Mostrar todas')
    print('3. Consultar habitación')
    print('4. Cambiar estado')
    print('5. Listar por estado')
    print('6. Salir')
 
 
# ─── Las 3 funciones de validación con excepciones propias ───────────────────
 
def validar_numero(numero):
    """Lanza NumeroInvalido si el número no tiene 3 dígitos (100-999)."""
    if not (100 <= numero <= 999):
        raise NumeroInvalido(f"Número inválido: {numero}. Debe tener 3 dígitos (100-999).")
    return numero
 
 
def validar_estado(estado):
    """Lanza EstadoInvalido si el estado no es 0 ni 1."""
    if estado != 0 and estado != 1:
        raise EstadoInvalido(f"Estado inválido: {estado}. Debe ser 0 (libre) o 1 (ocupada).")
    return estado
 
 
def validar_habitacion_existe(habitaciones, numero):
    """Lanza HabitacionNoExistente si no se encuentra la habitación."""
    for hab in habitaciones:
        if hab['numero'] == numero:
            return hab
    raise HabitacionNoExistente(f"La habitación {numero} no existe.")
 
 
# ─── Funciones de entrada ────────────────────────────────────────────────────
 
def pedir_numero_habitacion():
    while True:
        try:
            numero_input = int(input('Ingrese número de habitación: '))
            numero = validar_numero(numero_input)
            return numero
        except ValueError:
            print('Ingrese un número válido (solo dígitos).')
        except NumeroInvalido as e:
            print(f'Error: {e}')
 
 
def pedir_estado():
    while True:
        try:
            estado_input = int(input('Ingrese estado (0=libre, 1=ocupada): '))
            estado = validar_estado(estado_input)
            return estado
        except ValueError:
            print('Ingrese un número válido.')
        except EstadoInvalido as e:
            print(f'Error: {e}')
 
 
# ─── Operaciones del hotel ───────────────────────────────────────────────────
 
def agregar_habitacion(habitaciones):
    numero = pedir_numero_habitacion()
    try:
        validar_habitacion_existe(habitaciones, numero)
        print('La habitación ya existe.')
    except HabitacionNoExistente:
        estado = pedir_estado()
        habitaciones.append({'numero': numero, 'estado': estado})
        print('Habitación agregada.')
 
 
def mostrar_habitaciones(habitaciones):
    if not habitaciones:
        print('No hay habitaciones registradas.')
        return
    for hab in habitaciones:
        estado = 'Libre' if hab['estado'] == 0 else 'Ocupada'
        print(f'Habitación {hab["numero"]}: {estado}')
 
 
def consultar_habitacion(habitaciones):
    numero = pedir_numero_habitacion()
    try:
        hab = validar_habitacion_existe(habitaciones, numero)
        estado = 'Libre' if hab['estado'] == 0 else 'Ocupada'
        print(f'Habitación {numero}: {estado}')
    except HabitacionNoExistente as e:
        print(f'Error: {e}')
 
 
def cambiar_estado(habitaciones):
    numero = pedir_numero_habitacion()
    try:
        hab = validar_habitacion_existe(habitaciones, numero)
        estado = pedir_estado()
        hab['estado'] = estado
        print('Estado actualizado.')
    except HabitacionNoExistente as e:
        print(f'Error: {e}')
 
 
def listar_por_estado(habitaciones):
    estado = pedir_estado()
    filtradas = [h for h in habitaciones if h['estado'] == estado]
    if not filtradas:
        print('No hay habitaciones con ese estado.')
        return
    for hab in filtradas:
        texto = 'Libre' if hab['estado'] == 0 else 'Ocupada'
        print(f'Habitación {hab["numero"]}: {texto}')