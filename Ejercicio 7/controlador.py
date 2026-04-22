from vista import GastoVista

class GastoControlador:
    def __init__(self):
        self.gastos = []
        self.vista = GastoVista()

    def agregar_gasto(self, categoria, monto, fecha):
        from modelo import Gasto  # Importación local para evitar importación circular
        nuevo_gasto = Gasto(categoria, monto, fecha)
        self.gastos.append(nuevo_gasto)
        self.vista.mostrar_mensaje(f"Gasto agregado: {categoria} por ${monto}")

    def generar_reporte(self):
        resumen = {}
        for g in self.gastos:
            # Sumamos los montos por cada categoría
            resumen[g.categoria] = resumen.get(g.categoria, 0) + g.monto
        self.vista.mostrar_reporte(resumen)