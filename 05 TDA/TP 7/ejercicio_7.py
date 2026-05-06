asistencias = ["Ana", "Juan", "Pedro", "Ana", "Juan", "Ana"]
print(asistencias)

recuento = {}
for nombre in asistencias:
    if nombre in recuento:
        recuento[nombre] += 1
    else:
        recuento[nombre] = 1



una_vez = set(asistencias)

print(una_vez)

print(recuento)