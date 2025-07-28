from datetime import datetime

class Reporte:
    def __init__(self, esMalicioso, motivo, mensaje, tipo):
        self.esMalicioso = esMalicioso
        self.motivo = motivo
        self.fechaAnalisis = datetime.now()
        self.mensaje = mensaje
        self.tipo = tipo

    def emitirAlerta(self):
        print(f"ALERTA: {self.mensaje} ({self.motivo})")

    def bloquear(self):
        print(f"Enlace bloqueado")

    def mostrarReporte(self):
        print(f"   ¿Es malicioso?: {'Sí' if self.esMalicioso else 'No'}")
        print(f"   Motivo: {self.motivo}")
        print(f"   Tipo: {self.tipo}")
        print(f"   Mensaje: {self.mensaje}")
        print(f"   Fecha de análisis: {self.fechaAnalisis.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 20)