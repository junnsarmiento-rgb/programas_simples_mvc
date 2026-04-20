class Producto:
    def __init__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

    def actualizar_stock(self, cantidad):
        """Actualiza el stock (suma o resta según sea positivo o negativo)"""
        self.stock += cantidad

    def vender(self, cantidad):
        """Vende una cantidad del producto si hay stock disponible"""
        if cantidad > self.stock:
            return False, f"Stock insuficiente. Disponible: {self.stock}"
        self.stock -= cantidad
        return True, f"Venta realizada. Monto: ${cantidad * self.precio:.2f}"

    def reponer(self, cantidad):
        """Repone el stock del producto"""
        self.stock += cantidad
        return f"Stock repuesto. Nuevo stock: {self.stock}"

    def get_valor_total(self):
        """Calcula el valor total del producto en inventario"""
        return self.stock * self.precio

    def __str__(self):
        return f"{self.nombre} | Stock: {self.stock} | Precio: ${self.precio:.2f} | Total: ${self.get_valor_total():.2f}"
