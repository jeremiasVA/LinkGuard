from datetime import datetime
from LinkGuard.Datos.EnlaceDAO import EnlaceDAO

class Enlace:
    def __init__(self, url, estado):
        self.url = url
        self.estado = estado
        self.fechas = [datetime.now()]

    def setEstado(self, estado):
        self.estado = estado

    def setURL(self, url):
        self.url = url

    def getEstado(self):
        return self.estado

    def getURL(self):
        return self.url

    def registrarAcceso(self):
        self.fechas.append(datetime.now())

    def getFechas(self):
        return self.fechas
    
    def mostrarEnlace(self):
        print(f"   Enlace: {self.url}")
        print(f"   Estado: {self.estado}")
        print(f"   Fechas de acceso: ")
        for fecha in self.fechas:
            print(f"     - {fecha.strftime('%Y-%m-%d %H:%M:%S')}")
