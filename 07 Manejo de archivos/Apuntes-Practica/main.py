with open('C:\\Users\\Usuario\\Documents\\GitHub\\RepositorioUTNProgramacion1\\07 Manejo de archivos\\Apuntes-Practica\\usuarios.csv', 'r') as archivo:
    lineas = archivo.readlines()
    nombres = [linea.strip().split(',')[1] for linea in lineas[1:]]  # Omitir la línea de encabezado
    print(nombres)