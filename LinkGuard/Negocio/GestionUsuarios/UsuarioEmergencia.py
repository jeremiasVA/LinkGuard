from LinkGuard.Negocio.GestionUsuarios.Usuario import Usuario
from datetime import datetime

class UsuarioEmergencia(Usuario):
    def __init__(self, nombre, telefono, correo):
        super().__init__(nombre, telefono, correo)
        self.fechaReg = datetime.now()
    
    def recibirAlerta(self, mensaje):
        print("\nUsuario de Emergencia recibio una alerta:", mensaje)