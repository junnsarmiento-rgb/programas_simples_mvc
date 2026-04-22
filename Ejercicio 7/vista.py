class GastoVista:
    @staticmethod
    def mostrar_reporte(resumen):
        print("\n" + "="*35)
        print("   RESUMEN DE GASTOS POR CATEGORÍA")
        print("="*35)
        if not resumen:
            print("No hay gastos registrados.")
        else:
            for cat, total in resumen.items():
                print(f"• {cat:15}: ${total:,.2f}")
        print("="*35)

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f">>> {mensaje}")