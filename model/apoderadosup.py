from connection.connection import Conecction


class apoderadosSUp:
    def buscarApoderadosSup():
        query = "SELECT idapoderadosup, nombres, apellido_p, apellido_m, telefono, rut FROM apoderadosup"
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta)
        conexionBD.desconectar()
        return resultado

    def buscarApoderadoSup(id):
        query = "SELECT idapoderadosup, nombres, apellido_p, apellido_m, telefono, rut FROM apoderadosup WHERE idapoderadosup = %s"
        parametros = (id,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def crearApoderadoSup(
        nombres,
        apellido_p,
        apellido_m,
        telefono,
        rut,
    ):
        query = "INSERT INTO apoderadosup (nombres, apellido_p, apellido_m, telefono, rut) VALUES (%s,%s,%s,%s,%s);"
        tipoConsulta = 1
        parametros = (
            nombres,
            apellido_p,
            apellido_m,
            telefono,
            rut,
        )
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha insertado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la inserción", error)
        conexionBD.desconectar()

    def editarApoderadoSup(
        nombres,
        apellido_p,
        apellido_m,
        telefono,
        rut,
        idapoderado,
    ):
        query = "UPDATE befast.apoderadosup SET nombres=%s, apellido_p=%s, apellido_m=%s, telefono=%s, rut=%s WHERE idapoderadosup=%s;"
        tipoConsulta = 1
        parametros = (nombres, apellido_p, apellido_m, telefono, rut, idapoderado)
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha Editado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la edición", error)
        conexionBD.desconectar()

    def eliminarApoderadoSup(id):
        query = "DELETE FROM apoderadosup WHERE idapoderadosup = %s;"
        tipoConsulta = 1
        parametros = (id,)
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha Eliminado Correctamente")
        except:
            print("Ha ocurrido un problema en la Eliminación")
        conexionBD.desconectar()
