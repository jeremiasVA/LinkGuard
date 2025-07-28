class UsuarioDAO:
    def __init__(self):
        self.usuarios = []

    def agregarUsuario(self, usuario):
        if not self.buscarPorCorreo(usuario.getCorreo()):
            self.usuarios.append(usuario)
        else:
            print(f"Ya existe un usuario con el correo: {usuario.getCorreo()}")

    def obtenerUsuarios(self):
        return self.usuarios

    def buscarPorCorreo(self, correo):
        for user in self.usuarios:
            if user.getCorreo() == correo:
                return user
        return None

    def eliminarUsuario(self, correo):
        usuario = self.buscarPorCorreo(correo)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False
