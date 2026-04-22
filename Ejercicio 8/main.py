from controlador import JuegoControlador

def principal():
    # Instanciamos el controlador y arrancamos el juego
    juego = JuegoControlador()
    juego.iniciar()

if __name__ == "__main__":
    principal()