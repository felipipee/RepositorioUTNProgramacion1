class NotaInvalidaError(Exception):
    pass

def NotaInvalido(nota):
    if not (0 <= nota <= 10):
        
        return nota
    

nota = input("Ingrese la nota")
