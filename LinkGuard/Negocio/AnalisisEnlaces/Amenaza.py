class Amenaza:
    def __init__(self, tipo, descripcion, fuente):
        self.tipo = tipo
        self.descripcion = descripcion
        self.fuente = fuente

    def esCritica(self):
        return "phishing" in self.tipo.lower()

    def mostrarInformacion(self):
        return f"[Amenaza] Tipo: {self.tipo}, Fuente: {self.fuente}, Descripción: {self.descripcion}"
