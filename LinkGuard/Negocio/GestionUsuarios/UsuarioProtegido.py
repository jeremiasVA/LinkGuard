from LinkGuard.Negocio.GestionUsuarios.Usuario import Usuario
from LinkGuard.Negocio.DeteccionEnlaces.GestorEnlace import GestorEnlace
from LinkGuard.Negocio.GestionUsuarios.RegistroContacto import RegistroContacto
from datetime import datetime
        
class UsuarioProtegido(Usuario):
    def __init__(self, nombre, telefono, correo):
        super().__init__(nombre, telefono, correo)
        self.gestor = GestorEnlace()
        self.regContacto = RegistroContacto()
    
    def tieneContactoEmergencia(self):
        return len(self.regContacto.usuariosEm) > 0
    
    def marcarEnlaceSeguro(self, url):
        self.gestor.marcarEnlace(url, "Seguro")
    
    def marcarEnlaceInseguro(self, url):
        self.gestor.marcarEnlace(url, "Inseguro")
    
    def eliminarEnlace(self, url):
        self.gestor.eliminarEnlace(url)