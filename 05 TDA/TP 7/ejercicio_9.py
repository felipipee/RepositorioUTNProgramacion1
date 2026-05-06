agenda = {
    ("Lunes", "9:00"): "Reunión con el equipo",
    ("Lunes", "15:00"): "Entrenamiento en equipo",
    ("Martes", "14:00"): "Cita con el cliente",
    ("Miércoles", "9:00"): "Revisión de tareas",
    ("Miércoles", "11:00"): "Presentación del proyecto",
    ("Jueves", "16:00"): "Revisión de código",
    ("Viernes", "10:00"): "Planificación de la próxima semana"
}

consulta = input("Ingrese el dia a consultar (Lunes, Martes, Miércoles, Jueves, Viernes): ").capitalize()
if consulta in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
    print(f"Agenda para {consulta}:")
    for (dia, hora), actividad in agenda.items():
        if dia == consulta:
            print(f"{hora}: {actividad}")
else:
    print("Día no válido. Por favor, ingrese un día de la semana válido.")

