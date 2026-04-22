from modelo import Libro
from controlador import BibliotecaControlador

def ejecutar_programa():
    # Creamos los datos
    mis_libros = [
        Libro("Cien años de soledad", "García Márquez"),
        Libro("1984", "George Orwell"),
        Libro("El Principito", "Antoine de Saint-Exupéry")
    ]

    # Iniciamos el controlador
    app = BibliotecaControlador(mis_libros)

    # --- Acciones de prueba ---
    app.vista.mostrar_libros(mis_libros)
    app.prestar(0)
    app.vista.mostrar_libros(mis_libros)
    app.devolver(0)

if __name__ == "__main__":
    ejecutar_programa()