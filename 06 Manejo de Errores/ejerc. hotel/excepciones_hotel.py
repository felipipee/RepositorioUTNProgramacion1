class ErrorHotel(Exception):
    """Error base del hotel"""
    pass


class HabitacionNoExistente(ErrorHotel):
    pass

class NumeroInvalido(ErrorHotel):
    pass

class EstadoInvalido(ErrorHotel):
    pass