class Usuario:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def getNombre(self):
        return self.nombre
    
    def getTelefono(self):
        return self.telefono
    
    def getCorreo(self):
        return self.correo

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTelefono(self, telefono):
        self.telefono = telefono
    
    def setCorreo(self, correo):
        self.correo = correo
class UsuarioEmergencia(Usuario):
    def __init__(self, nombre, telefono, correo):
        super().__init__(nombre, telefono, correo)
        self.fechaReg = datetime.now()
    
    def recibirAlerta(mensaje):
        print("Usuario de Emergencia recibio una alerta:")
        print(mensaje)
