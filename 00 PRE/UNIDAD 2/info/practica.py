nota=float(input("Ingrese su nota: "))

if nota <= 90 and nota < 100:
    print("Exelente")
elif nota > 80 and nota < 89:
    print("Muy bueno")
elif nota > 70 and nota < 79:
    print("Bueno")
elif nota > 60 and nota < 69:
    print("Suficiente")
elif nota > 0 and nota < 59:
    print("Insuficiente")

