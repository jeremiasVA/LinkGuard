from LinkGuard.Negocio.AnalisisEnlaces.MotorDeteccion import MotorDeteccion
from LinkGuard.Negocio.GestionHistorial.Historial import Historial

class GestorEnlace:
    def __init__(self):
        self.motor = MotorDeteccion()
        self.historialDeteccion = Historial()

    def interceptarEnlace(self, url):
        print(f"Interceptando enlace: {url}")

        registro = self.historialDeteccion.consultarEnlace(url)
        if registro:
            print("El enlace ya existe en el historial")
            (enlace, reporteAnterior) = registro
            enlace.registrarAcceso()
            if enlace.getEstado() == "Inseguro":
                print("Analisis previo: ", enlace.getEstado())
                reporteAnterior.emitirAlerta()
                reporteAnterior.bloquear()
            else:
                print("Resultado previo:", enlace.getEstado(), "\n se permite el acceso")
            return reporteAnterior

        reporte = self.motor.analizarEnlace(url)
        self.historialDeteccion.agregarEnlace(url, reporte)
        return reporte

    def enlaceEnHistorial(self, url):
        print(url)
        registro = self.historialDeteccion.consultarEnlace(url)
        if registro:
            return registro
        return None

    def marcarEnlace(self, url, estado):
        registro = self.enlaceEnHistorial(url)
        if registro:
            (enlace, reporte) = registro
            enlace.setEstado(estado)
            reporte.esMalicioso = estado == "Inseguro"

    def eliminarEnlace(self, enlace):
        self.historialDeteccion.eliminarEnlace(enlace)
