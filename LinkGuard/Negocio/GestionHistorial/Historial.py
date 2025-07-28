from LinkGuard.Negocio.GestionHistorial.Enlace import Enlace
from LinkGuard.Negocio.GestionAlertas.Reporte import Reporte
from LinkGuard.Datos.HistorialDAO import HistorialDAO
from LinkGuard.Datos.EnlaceDAO import EnlaceDAO

class Historial:
    def __init__(self):
        self.enlaces = []
        self.historialDAO = HistorialDAO()
        self.enlaceDAO = EnlaceDAO()

    def consultarEnlace(self, url):
        for registro in self.historialDAO.obtenerHistorial():
            (enlace, reporte) = registro
            if enlace.getURL() == url:
                return (enlace, reporte)
        return None

    def actualizarHistorial(self, enlace, reporte):
        self.historialDAO.agregarRegistro(enlace, reporte)

    def agregarEnlace(self, url, reporte):
        enlace = Enlace(url, "Inseguro" if reporte.esMalicioso else "Seguro")
        self.enlaces.append((enlace, reporte))
        self.enlaceDAO.agregarEnlace(enlace)
        self.actualizarHistorial(enlace, reporte)
        return enlace
        
    def getHistorial(self):
        return self.historialDAO.obtenerHistorial()
    
    def eliminarEnlace(self, enlace):
        self.enlaces = [(e, r) for (e, r) in self.enlaces if e.getURL() != enlace.getURL()]
        self.historialDAO.historial = [
            (e, r) for (e, r) in self.historialDAO.obtenerHistorial() if e.getURL() != enlace.getURL()
        ]