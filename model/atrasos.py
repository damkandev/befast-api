from connection.connection import Conecction


class atrasos:
    def buscarAtrasos():
        query = "SELECT e.idestudiante, e.nombres, e.apellido_p, e.apellido_m, e.avatar, c.nivel, c.letra, e.rut, a.fecha_atraso, a.hora_atraso FROM estudiante e RIGHT JOIN atraso a ON e.idestudiante = a.idestudiante LEFT JOIN curso c ON e.idcurso = c.idcurso"
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta)
        conexionBD.desconectar()
        return resultado

    def buscarAtraso(id):
        query = "SELECT e.idestudiante, e.nombres, e.apellido_p, e.apellido_m, e.avatar, c.nivel, c.letra, e.rut, a.fecha_atraso, a.hora_atraso FROM estudiante e RIGHT JOIN atraso a ON e.idestudiante = a.idestudiante LEFT JOIN curso c ON e.idcurso = c.idcurso WHERE e.idestudiante = %s"
        parametros = (id,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def crearAtraso(
        idcurso,
        idestudiante,
        idinspector,
        fecha_atraso,
        hora_atraso,
    ):
        query = "INSERT INTO atraso (idcurso, idestudiante, idinspector, fecha_atraso, hora_atraso) VALUES (%s,%s,%s,%s,%s);"
        tipoConsulta = 1
        parametros = (idcurso, idestudiante, idinspector, fecha_atraso, hora_atraso)
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha insertado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la inserción", error)
        conexionBD.desconectar()

    def editarAtraso(
        idcurso, idestudiante, idinspector, fecha_atraso, hora_atraso, idatraso
    ):
        query = "UPDATE atraso SET idcurso = %s, idestudiante=%s, idinspector=%s, fecha_atraso=%s, hora_atraso=%s WHERE idatraso=%s;"
        tipoConsulta = 1
        parametros = (
            idcurso,
            idestudiante,
            idinspector,
            fecha_atraso,
            hora_atraso,
            idatraso,
        )
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha Editado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la edición", error)
        conexionBD.desconectar()

    def eliminarAtraso(id):
        query = "DELETE FROM atraso WHERE idatraso = %s;"
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
