from model.usuarios import Usuarios
class handleUsers:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
      
    def buscarUsuarios():
        datos = Usuarios.buscarUsuarios()
        usuarios = []
        for usuario in datos:
            _usuario = {
                "id": usuario[0],
                "nombre": usuario[1],
                "correo": usuario[2],
                "contraseña": usuario[3],
                "role": usuario[4],
                "payed": usuario[5]
            }
            usuarios.append(_usuario)
        return usuarios