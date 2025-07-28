from LinkGuard.Negocio.AnalisisEnlaces.Amenaza import Amenaza
from LinkGuard.Negocio.GestionAlertas.Reporte import Reporte

class MotorDeteccion:
    def __init__(self, tipo="Detector de amenazas"):
        self.tipo = tipo

    def analizarEnlace(self, url):
        amenazas = self.detectarAmenazas(url)
        if amenazas:
            amenaza = amenazas[0]  # Tomamos solo la primera amenaza para el reporte
            mensaje = amenaza.descripcion.upper()
            reporte = Reporte(True, amenaza.descripcion, mensaje, amenaza.tipo)
            reporte.emitirAlerta()
            reporte.bloquear()
        else:
            mensaje = "Enlace seguro"
            reporte = Reporte(False, "Ninguna", mensaje, "Ninguna")
            print("No se encontraron amenazas, se permite el acceso")
        return reporte

    def detectarAmenazas(self, url):
        print("Buscando amenazas")
        amenazas = []

        # Amenazas personalizadas por URL
        if "malicioso1.com" in url:
            amenazas.append(Amenaza("Phishing", "Enlace falso para robar credenciales", url))
        elif "phishing.com" in url:
            amenazas.append(Amenaza("Phishing", "Enlace diseñado para imitar sitios legítimos", url))
        elif "fraude.net" in url:
            amenazas.append(Amenaza("Fraude", "Sitio sospechoso de estafas económicas", url))
        elif "fakebank.com" in url:
            amenazas.append(Amenaza("Phishing", "Simulación de entidad bancaria", url))
        elif "smishing.org" in url:
            amenazas.append(Amenaza("Smishing", "Engaño a través de mensajes SMS", url))
        elif not url.startswith("https://"):
            amenazas.append(Amenaza("Phishing", "Enlace sin cifrado seguro (http)", url))

        return amenazas
