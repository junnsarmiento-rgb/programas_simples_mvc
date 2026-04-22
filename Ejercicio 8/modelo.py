import random

class JuegoModelo:
    def __init__(self):
        # El modelo genera el número aleatorio al iniciar
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validar_intento(self, suposicion):
        self.intentos += 1
        if suposicion < self.numero_secreto:
            return "Muy bajo"
        elif suposicion > self.numero_secreto:
            return "Muy alto"
        else:
            return "Correcto"