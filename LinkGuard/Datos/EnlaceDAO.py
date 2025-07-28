class EnlaceDAO:
    def __init__(self):
        self.enlaces = []

    def agregarEnlace(self, enlaceNuevo):
        for i, enlace in enumerate(self.enlaces):
            if enlace.getURL() == enlaceNuevo.getURL():
                self.enlaces[i] = enlaceNuevo
                return
        self.enlaces.append(enlaceNuevo)


    def listarEnlaces(self):
        return self.enlaces