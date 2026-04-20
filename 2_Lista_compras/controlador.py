from modelo import Producto
from vista import Vista

class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.lista_productos = []

    def agregar_producto(self):
        """Agrega un nuevo producto a la lista"""
        nombre, cantidad = self.vista.pedir_datos_producto()
        producto = Producto(nombre, cantidad)
        self.lista_productos.append(producto)
        print(f"Producto '{nombre}' agregado exitosamente.")

    def eliminar_producto(self):
        """Elimina un producto de la lista"""
        self.vista.mostrar_lista(self.lista_productos)
        if not self.lista_productos:
            return

        indice = self.vista.pedir_indice_producto(
            self.lista_productos,
            "Ingrese el número del producto a eliminar: "
        )

        if indice is not None:
            producto_eliminado = self.lista_productos.pop(indice)
            print(f"Producto '{producto_eliminado.nombre}' eliminado exitosamente.")

    def marcar_comprado(self):
        """Marca un producto como comprado"""
        # Mostrar solo productos pendientes
        pendientes = [p for p in self.lista_productos if not p.comprado]
        if not pendientes:
            print("No hay productos pendientes para marcar como comprados.")
            return

        print("\nPRODUCTOS PENDIENTES:")
        for i, producto in enumerate(pendientes, 1):
            print(f"{i}. {producto.nombre} - Cantidad: {producto.cantidad}")

        indice = self.vista.pedir_indice_producto(
            pendientes,
            "Ingrese el número del producto a marcar como comprado: "
        )

        if indice is not None:
            pendientes[indice].marcar_comprado()
            print(f"Producto '{pendientes[indice].nombre}' marcado como comprado.")

    def mostrar_lista(self):
        """Muestra la lista de productos"""
        self.vista.mostrar_lista(self.lista_productos)

    def ejecutar(self):
        """Ejecuta el programa principal"""
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == 1:
                self.agregar_producto()
            elif opcion == 2:
                self.eliminar_producto()
            elif opcion == 3:
                self.marcar_comprado()
            elif opcion == 4:
                self.mostrar_lista()
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

            input("\nPresione Enter para continuar...")