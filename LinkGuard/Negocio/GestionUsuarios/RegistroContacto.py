from LinkGuard.Datos.UsuarioDAO import UsuarioDAO
from datetime import datetime

class RegistroContacto:
    def __init__(self):
        self.fechaRegistro = datetime.now()
        self.usuariosEm = []
        self.usuarioDAO = UsuarioDAO()

    def agregarUsuarioEmergencia(self, usuario):
        self.usuariosEm.append(usuario)
        if self.validarContactoExistente(usuario.getTelefono(), usuario.getCorreo()):
            print("El usuario de emergencia ya existe, agregue uno nuevo o modifique el contacto")
            return
        print("Se ha registrado al usuario de Emergencia: ", usuario.getNombre())
        self.usuarioDAO.agregarUsuario(usuario)
    
    def eliminarUsuarioEmergencia(self, usuario):
        for userEm in self.usuariosEm:
            if (
                usuario.getNombre() == userEm.getNombre()
                and usuario.getTelefono() == userEm.getTelefono()
                and usuario.getCorreo() == userEm.getCorreo()
            ):
                self.usuariosEm.remove(userEm)
                print("Usuario de emergencia eliminado")
                return
        print("Usuario no encontrado")

    def getContactosEmergencia(self):
        return self.usuariosEm
    
    def validarContactoExistente(self, telefono, correo):
        for userEm in self.usuariosEm:
            if userEm.getTelefono()==telefono and userEm.getCorreo()==correo:
                return True
        return False
    
    def buscarContactoPorTelefono(self, telefono):
        for userEm in self.usuariosEm:
            if userEm.getTelefono() == telefono:
                return userEm
        return None
    
    def buscarContactoPorCorreo(self, correo):
        for userEm in self.usuariosEm:
            if userEm.getCorreo() == correo:
                return userEm
        return None
    
    def notificarUsuariosEmergencia(self, reporte, usuarioProtegido):
        for user in self.usuariosEm:
            mensaje = (
                f"\nNotificando a: {user.getNombre()} ({user.getCorreo()})\n"
                f"El usuario {usuarioProtegido} ha intentado entrar a un enlace malicioso.\n"
                f"Se ha bloqueado el acceso al enlace.\n"
                f"Mensaje: {reporte.mensaje}\n"
                f"Tipo de amenaza: {reporte.tipo}\n"
                f"Motivo: {reporte.motivo}\n"
                f"Fecha: {reporte.fechaAnalisis.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            user.recibirAlerta(mensaje)