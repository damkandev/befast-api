from connection.connection import Conecction


class apoderados:
    def buscarApoderados():
        query = "SELECT idapoderado, nombres, apellido_p, apellido_m, telefono, rut FROM apoderado"
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta)
        conexionBD.desconectar()
        return resultado

    def buscarApoderado(id):
        query = "SELECT idapoderado, nombres, apellido_p, apellido_m, telefono, rut FROM apoderado WHERE idapoderado = %s"
        parametros = (id,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def crearApoderado(
        nombres,
        apellido_p,
        apellido_m,
        telefono,
        rut,
    ):
        query = "INSERT INTO apoderado (nombres, apellido_p, apellido_m, telefono, rut) VALUES (%s,%s,%s,%s,%s);"
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

    def editarApoderado(
        nombres,
        apellido_p,
        apellido_m,
        telefono,
        rut,
        idapoderado,
    ):
        query = "UPDATE befast.apoderado SET nombres=%s, apellido_p=%s, apellido_m=%s, telefono=%s, rut=%s WHERE idapoderado=%s;"
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

    def eliminarApoderado(id):
        query = "DELETE FROM apoderado WHERE idapoderado = %s;"
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
