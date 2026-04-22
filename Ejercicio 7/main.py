from controlador import GastoControlador

def ejecutar_app_gastos():
    # Iniciamos el sistema de control
    control = GastoControlador()

    # --- Simulando entrada de datos ---
    control.agregar_gasto("Alimentación", 25000, "2026-04-20")
    control.agregar_gasto("Transporte", 12000, "2026-04-20")
    control.agregar_gasto("Entretenimiento", 45000, "2026-04-21")
    control.agregar_gasto("Alimentación", 15000, "2026-04-21")

    # Generamos el reporte final
    control.generar_reporte()

if __name__ == "__main__":
    ejecutar_app_gastos()