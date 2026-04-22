class JuegoVista:
    @staticmethod
    def solicitar_numero():
        try:
            return int(input("\nIntroduce un número (1-100): "))
        except ValueError:
            print("❌ Por favor, ingresa solo números enteros.")
            return None

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f">>> {mensaje}")

    @staticmethod
    def bienvenida():
        print("\n" + "!" * 25)
        print(" ¡ADIVINA EL NÚMERO! ")
        print("!" * 25)