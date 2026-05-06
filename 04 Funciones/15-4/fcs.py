def calcular_promedio(notas):
    print("Calcular Promedio")
    divisor = len(notas)
    suma = sum(notas)
    promedio = suma / divisor
    print(f"promedio: {promedio}")

def calcular_promedio_2(notas):
    print("Calcular Promedio")
    divisor = len(notas)
    suma = sum(notas)
    promedio = suma / divisor
    print(f"promedio: {promedio}")

def aprobados(notas):
    print("Alumnos Aprobados")
    
    aprobados = []
    for nota in notas:
        if nota >= 6:
            aprobados.append(nota)
    aprobados_cant = len(aprobados)
    print(f"Cantidad de alumnos aprobados: {aprobados_cant}")
    multiplicacion = aprobados_cant * 100
    porcentaje = multiplicacion / len(notas)
    print(f"Porcentaje de alumnos aprobados: {porcentaje:.2f}%")



def nota_maxima(notas):
    print("Nota Máxima")
    nota_max = max(notas)
    print(f"La nota máxima es: {nota_max}")

def nota_minima(notas):
    print("Nota Mínima")
    nota_min = min(notas)
    print(f"La nota mínima es: {nota_min}")

def analizar_notas(notas):
    print("Análisis de Notas")
    calcular_promedio_2(notas)
    nota_maxima(notas)
    nota_minima(notas)