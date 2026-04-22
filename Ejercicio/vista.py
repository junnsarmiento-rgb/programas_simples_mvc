class BibliotecaVista:
    @staticmethod
    def mostrar_libros(libros):
        print("\n" + "="*30)
        print("   CATÁLOGO DE LIBROS")
        print("="*30)
        for i, libro in enumerate(libros):
            estado = "✅" if libro.disponible else "❌"
            print(f"{i}. {estado} {libro.titulo} - {libro.autor}")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f">>> {mensaje}")