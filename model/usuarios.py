import os
from connection.connection import Conecction
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import base64

connection = Conecction()

load_dotenv()


def cargar_clave():
    clave = os.getenv("CLAVE_ENCRIPTACION").encode()
    return clave


def encriptar(contrasena, clave):
    crypter = Fernet(base64.urlsafe_b64encode(clave.ljust(32, b"\0")))
    ce = crypter.encrypt((contrasena.encode()))
    return ce


def desencriptar(contrasena, clave):
    crypter = Fernet(base64.urlsafe_b64encode(clave.ljust(32, b"\0")))
    cd = crypter.decrypt(contrasena.encode())
    return cd


class Usuarios:
    def registrarUsuario(nombre, correo, contrasena):
        contrasenaEncriptada = encriptar(contrasena, cargar_clave())
        query = "INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)"
        parametros = nombre, correo, contrasenaEncriptada
        connection.conectar()
        resultado = connection.consultaDB(query, 1, parametros)
        connection.desconectar()
        return resultado

    def iniciarSesion(correo, contrasena):
        query = "SELECT * FROM usuarios WHERE correo = %s"
        parametros = (correo,)
        connection.conectar()
        contrasenaValida = False
        resultado = connection.consultaDB(query, 2, parametros)
        contrasenaDesencriptada = desencriptar(resultado[0][3], cargar_clave())
        if str(contrasenaDesencriptada, "utf8") == contrasena:
            contrasenaValida = True
        else:
            contrasenaValida = False
        return contrasenaValida
