from modelo import Tarea


class Vista:
    def __init__(self):
        pass

    def mostrar_lista(self, tareas):
        """Muestra la lista de tareas organizadas por estado"""
        if not tareas:
            print("La lista de tareas está vacía.")
            return

        print("\n" + "="*60)
        print("              LISTA DE TAREAS")
        print("="*60)

        pendientes = [t for t in tareas if not t.estado]
        completadas = [t for t in tareas if t.estado]

        if pendientes:
            print("\nPENDIENTES:")
            for i, tarea in enumerate(pendientes, 1):
                print(f"{i}. {tarea}")

        if completadas:
            print("\nCOMPLETADAS:")
            for i, tarea in enumerate(completadas, 1):
                print(f"{i}. {tarea}")

        print("\n" + "="*60)

    def mostrar_menu(self):
        """Muestra el menú de opciones"""
        print("\n" + "="*40)
        print("        MENÚ DE TAREAS")
        print("="*40)
        print("1. Crear nueva tarea")
        print("2. Completar tarea")
        print("3. Eliminar tarea")
        print("4. Marcar como pendiente")
        print("5. Mostrar lista")
        print("6. Salir")
        print("="*40)

    def pedir_opcion(self):
        """Pide al usuario que seleccione una opción"""
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            return opcion
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return None

    def pedir_descripcion_tarea(self):
        """Pide la descripción de una nueva tarea"""
        descripcion = input("Descripción de la tarea: ").strip()
        while not descripcion:
            descripcion = input(
                "La descripción no puede estar vacía. Descripción de la tarea: ").strip()
        return descripcion

    def pedir_indice_tarea(self, tareas, mensaje):
        """Pide el índice de una tarea de la lista"""
        if not tareas:
            print("No hay tareas en la lista.")
            return None

        try:
            indice = int(input(mensaje)) - 1
            if 0 <= indice < len(tareas):
                return indice
            else:
                print("Índice fuera de rango.")
                return None
        except ValueError:
            print("Índice inválido.")
            return None
