from connection.connection import Conecction
connection = Conecction()

class Usuarios:
    def buscarUsuarios():
        query = "SELECT * FROM usuarios"
        connection.conectar()
        resultado = connection.consultaDB(query, 2)
        connection.desconectar()
        return resultado
        
    def buscarUsuario(id):
        query = "SELECT * FROM usuarios WHERE userid = %s"
        parametros = id,
        connection.conectar()
        resultado = connection.consultaDB(query, 2, parametros)
        connection.desconectar()
        return resultado
    
    def registrarUsuario(nombre, correo, contrasena):
        query = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)" 
        parametros = nombre, correo, contrasena
        connection.conectar()
        resultado = connection.consultaDB(query, 1, parametros)
        connection.desconectar()
        return resultado
