from modelo import Producto

class Vista:
    def __init__(self):
        pass

    def mostrar_lista(self, pendientes, comprados):
        """Muestra la lista de compras organizada por estado"""
        if not pendientes and not comprados:
            print("La lista de compras está vacía.")
            return

        print("\n" + "="*50)
        print("         LISTA DE COMPRAS")
        print("="*50)

        if pendientes:
            print("\nPENDIENTES:")
            for i, producto in enumerate(pendientes, 1):
                print(f"{i}. {producto}")

        if comprados:
            print("\nCOMPRADOS:")
            for i, producto in enumerate(comprados, 1):
                print(f"{i}. {producto}")

        print("\n" + "="*50)

    def mostrar_menu(self):
        """Muestra el menú de opciones"""
        print("\n" + "="*30)
        print("     MENÚ DE OPCIONES")
        print("="*30)
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Marcar producto como comprado")
        print("4. Mostrar lista")
        print("5. Salir")
        print("="*30)

    def pedir_opcion(self):
        """Pide al usuario que seleccione una opción"""
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            return opcion
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return None

    def pedir_datos_producto(self):
        """Pide los datos para crear un nuevo producto"""
        nombre = input("Nombre del producto: ").strip()
        while not nombre:
            nombre = input("El nombre no puede estar vacío. Nombre del producto: ").strip()

        try:
            cantidad = int(input("Cantidad: "))
            while cantidad <= 0:
                cantidad = int(input("La cantidad debe ser mayor a 0. Cantidad: "))
            return nombre, cantidad
        except ValueError:
            print("Cantidad inválida. Intente nuevamente.")
            return self.pedir_datos_producto()

    def pedir_indice_producto(self, lista_productos, mensaje):
        """Pide el índice de un producto de la lista"""
        if not lista_productos:
            print("No hay productos en la lista.")
            return None

        try:
            indice = int(input(mensaje)) - 1
            if 0 <= indice < len(lista_productos):
                return indice
            else:
                print("Índice fuera de rango.")
                return None
        except ValueError:
            print("Índice inválido.")
            return None