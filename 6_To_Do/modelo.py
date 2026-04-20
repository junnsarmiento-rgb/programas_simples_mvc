class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = False  # False = pendiente, True = completada

    def completar(self):
        self.estado = True

    def marcar_pendiente(self):
        self.estado = False

    def __str__(self):
        estado = "[bien]" if self.estado else "[ ]"
        descripcion = self.descripcion
        if self.estado:
            descripcion = f"~{self.descripcion}~"
        return f"{estado} {descripcion}"
