# Ejercicio 1: Crear un diccionario con los precios de algunas frutas y agregar otras frutas con sus precios al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
print(precios_frutas)
precios_frutas.update(Naranja = 1200, Manzana = 1500, Pera = 2300)
print(precios_frutas)


#Ejercicio 2: Modificar los precios de algunas frutas
precios_frutas.update(Banana = 1330, Manzana = 1700, Melón = 2800)
print(precios_frutas)


# Ejercicio 3: Obtener las claves del diccionario
lista = list(precios_frutas.keys())
print(lista)