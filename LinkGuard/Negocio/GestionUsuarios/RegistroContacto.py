from datetime import datetime

class RegistroContacto:
    def __init__(self):
        self.fechaRegistro = datetime.now()
        self.usuariosEm = []

    def agregarUsuarioEmergencia(self, usuario):
        self.usuariosEm.append(usuario)
        if self.validarContactoExistente(usuario.getTelefono(), usuario.getCorreo()):
            print("El usuario de emergencia ya existe, agregue uno nuevo o modifique el contacto")
            return
        print("Se ha registrado al usuario de Emergencia: ", usuario.getNombre())
    
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