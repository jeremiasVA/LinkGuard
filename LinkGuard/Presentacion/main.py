from LinkGuard.Negocio.DeteccionEnlaces.GestorEnlace import GestorEnlace
from LinkGuard.Negocio.GestionUsuarios.Usuario import UsuarioProtegido, UsuarioEmergencia
from LinkGuard.Negocio.GestionHistorial.Enlace import Enlace

def mostrarMenuPrincipal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ingresar enlace")
    print("2. Usuarios de Emergencia")
    print("3. Ver historial de enlaces")
    print("4. Salir")

def mostrarSubmenuEnlaces():
    print("\n--- INGRESAR ENLACE ---")
    enlaces = [
        "http://malicioso1.com",
        "http://phishing.com",
        "http://fraude.net",
        "http://fakebank.com",
        "http://smishing.org",
        "https://google.com",
        "https://wikipedia.org",
        "https://openai.com",
        "https://github.com",
        "https://python.org"
    ]
    for i, enlace in enumerate(enlaces, start=1):
        print(f"{i}. {enlace}")
    print("11. Volver al menú principal")
    return enlaces

def ingresarEnlace(usuarioProtegido):
    gestor = usuarioProtegido.gestor
    enlaces = mostrarSubmenuEnlaces()
    while True:
        opcion = input("Selecciona un enlace (1-10) o 11 para volver: ")
        if opcion == "11":
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= 10:
            url = enlaces[int(opcion) - 1]
            reporte = gestor.interceptarEnlace(url)

            if reporte.esMalicioso:
                contactosEmergencia = usuarioProtegido.regContacto.getContactosEmergencia()
                if len(contactosEmergencia) > 0:
                    notificar = input("¿Deseas notificar a los usuarios de emergencia? (s/n): ").lower()
                    if notificar == "s":
                        print("\n--- NOTIFICACION A USUARIOS DE EMERGENCIA ---")
                        usuarioProtegido.regContacto.notificarUsuariosEmergencia(reporte, usuarioProtegido.getNombre())
            
            print(f"\nEnlace '{url}' procesado")
            print("---------------------------")
        else:
            print("Opcion invalida")


def verUsuariosEmergencia(usuarioProtegido):
    while True:
        usuarios = usuarioProtegido.regContacto.getContactosEmergencia()
        print("\n--- USUARIOS DE EMERGENCIA ---")
        
        if len(usuarios) == 0:
            print("No hay usuarios de emergencia registrados")
        else:
            for i, user in enumerate(usuarios, 1):
                print(f"{i}. {user.getNombre()} - {user.getTelefono()} - {user.getCorreo()}")

        print(f"{len(usuarios)+1}. Agregar nuevo usuario de emergencia")
        print(f"{len(usuarios)+2}. Volver al menu principal")

        opcion = input("Selecciona una opcion: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(usuarios):
                gestionarUsuarioEmergencia(usuarioProtegido.regContacto, usuarios[opcion-1])
            elif opcion == len(usuarios) + 1:
                registrarUsuarioEmergencia(usuarioProtegido)
            elif opcion == len(usuarios) + 2:
                break
            else:
                print("Opcion invalida")
        else:
            print("Ingresa un numero valido")

def registrarUsuarioEmergencia(usuarioProtegido):
    print("\n--- REGISTRAR USUARIO DE EMERGENCIA ---")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    correo = input("Correo electronico: ")
    usuarioEmergencia = UsuarioEmergencia(nombre, telefono, correo)
    usuarioProtegido.regContacto.agregarUsuarioEmergencia(usuarioEmergencia)
    print("Usuario de emergencia registrado con exito")


def gestionarUsuarioEmergencia(regContacto, usuario):
    while True:
        print(f"\n--- GESTIONAR USUARIO ---\nNombre: {usuario.getNombre()}\nTeléfono: {usuario.getTelefono()}\nCorreo: {usuario.getCorreo()}")
        print("1. Modificar")
        print("2. Eliminar")
        print("3. Volver")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nuevoNombre = input("Nuevo nombre: ")
            nuevoTelefono = input("Nuevo teléfono: ")
            nuevoCorreo = input("Nuevo correo: ")
            usuario.setNombre(nuevoNombre)
            usuario.setTelefono(nuevoTelefono)
            usuario.setCorreo(nuevoCorreo)
            print("Usuario modificado con exito")
        elif opcion == "2":
            regContacto.eliminarUsuarioEmergencia(usuario)
            print("Usuario eliminado con exito")
            break
        elif opcion == "3":
            break
        else:
            print("Opcion invalida")


def verHistorial(usuarioProtegido):
    historial = usuarioProtegido.gestor.historialDeteccion.historialDAO.obtenerHistorial()

    if not historial:
        print("\nHistorial vacio")
        return
    
    while True:
        historial = usuarioProtegido.gestor.historialDeteccion.historialDAO.obtenerHistorial()

        print("\n--- HISTORIAL DE ENLACES ---")
        for i, (enlace, reporte) in enumerate(historial, start=1):
            estado = enlace.getEstado()
            print(f"{i}. {enlace.getURL()} - {estado}")
        print(f"{len(historial)+1}. Volver al menu principal")

        opcion = input("Selecciona un enlace para gestionar o volver: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(historial):
                enlace, reporte = historial[opcion - 1]
                gestionarEnlace((enlace, reporte), usuarioProtegido)
            elif opcion == len(historial) + 1:
                break
            else:
                print("Opcion invalida")
        else:
            print("Entrada invalida")


def gestionarEnlace(registro, usuarioProtegido):
    (enlace, reporte) = registro
    while True:
        print(f"\n--- GESTIONAR ENLACE ---\n{enlace.getURL(), enlace.getEstado()}\nMensaje: {reporte.mensaje} tipo: {reporte.tipo}")
        print("1. Marcar como seguro")
        print("2. Marcar como inseguro")
        print("3. Ver detalles")
        print("4. Eliminar")
        print("5. Volver")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            usuarioProtegido.marcarEnlaceSeguro(enlace.getURL())
            print("Enlace marcado como seguro")
        elif opcion == "2":
            usuarioProtegido.marcarEnlaceInseguro(enlace.getURL())
            print("Enlace marcado como inseguro")
        elif opcion == "3":
            enlace.mostrarEnlace()
            reporte.mostrarReporte()
        elif opcion == "4":
            usuarioProtegido.eliminarEnlace(enlace)
            print("Enlace eliminado del historial")
            break
        elif opcion == "5":
            break
        else:
            print("Opcion invalida")

def main():
    usuarioProtegido = UsuarioProtegido("Jaimito", 77426434, "jaimigomez3@gmail.com")
    while True:
        mostrarMenuPrincipal()
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            ingresarEnlace(usuarioProtegido)
        elif opcion == "2":
            verUsuariosEmergencia(usuarioProtegido)
        elif opcion == "3":
            verHistorial(usuarioProtegido)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intenta nuevamente")

if __name__ == "__main__":
    main()
