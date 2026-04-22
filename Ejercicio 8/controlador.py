from vista import JuegoVista
from modelo import JuegoModelo

class JuegoControlador:
    def __init__(self):
        self.modelo = JuegoModelo()
        self.vista = JuegoVista()

    def iniciar(self):
        self.vista.bienvenida()
        acertado = False

        while not acertado:
            intento = self.vista.solicitar_numero()
            
            if intento is not None:
                resultado = self.modelo.validar_intento(intento)
                self.vista.mostrar_mensaje(resultado)
                
                if resultado == "Correcto":
                    acertado = True
                    self.vista.mostrar_mensaje(f"¡Felicidades! Lo lograste en {self.modelo.intentos} intentos.")