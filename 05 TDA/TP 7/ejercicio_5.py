print("Recuento de palabras")



frase = input("Ingrese una frase: ")
while not frase.replace(" ", "").isalpha():
    print("Error, ingrese solo texto")
    frase = input("Ingrese una frase: ")

palabras = frase.split()
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento de palabras:")
for palabra, cantidad in recuento.items():
    print(f"{palabra}: {cantidad}")