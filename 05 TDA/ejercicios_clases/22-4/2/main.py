estudiantes = { 
    "Ana": [7, 8, 9], 
    "Luis": [6, 7, 5], 
    "Marta": [10, 9, 9] 
}

promedios = []
copia: list = estudiantes.values()
copia = list(copia)

nombres: dict = estudiantes.keys()
nombres = list(nombres)


for i in range(len(copia)):
    suma = sum(copia[i])
    division = suma / 3
    promedios.append(division)
    print(f"{nombres[i]}, {division}")

promedio_alto = max(promedios)
promedio_bajo = min(promedios)

indice = promedios.index(promedio_alto)
print(f"{nombres[indice]}, {promedio_alto}")

aprobados = []
if promedios[i] >= 6.0:
    aprobados.append(promedios[i])

for i in range(len(promedios)):
    if promedios[i] >= 6.0:
        print(f"{nombres[i]}, {promedios[i]}")

lista_tuplas = []
for i in range(len(promedios)):
    tupla = (nombres[i], max(promedios))
    promedios.remove(max(promedios))
    lista_tuplas.append(tupla)

print(lista_tuplas)
