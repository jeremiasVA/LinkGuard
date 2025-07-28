class HistorialDAO:
    def __init__(self):
        self.historial: list[tuple] = []

    def agregarRegistro(self, enlace, reporte):
        self.historial.append((enlace, reporte))
