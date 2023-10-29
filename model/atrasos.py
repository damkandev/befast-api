from connection.connection import Conecction


class atrasos:
    def buscarAtrasos():
        query = "SELECT e.nombres, e.apellido_p, e.apellido_m, c.nivel, c.letra, e.rut, e.avatar, a.fecha, a.hora, a.idatraso, a.idestudiante FROM atrasos a LEFT JOIN estudiante e ON a.idestudiante = e.idestudiante LEFT JOIN curso c ON e.idcurso = c.idcurso"
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta)
        conexionBD.desconectar()
        return resultado

    def buscarAtraso(termino):
        query = f"SELECT e.nombres, e.apellido_p, e.apellido_m, c.nivel, c.letra, e.rut, e.avatar, a.fecha, a.hora, a.idatraso, a.idestudiante FROM atrasos a LEFT JOIN estudiante e ON a.idestudiante = e.idestudiante LEFT JOIN curso c ON e.idcurso = c.idcurso WHERE e.nombres LIKE '%{termino}%' OR e.apellido_p LIKE '%{termino}%' OR e.apellido_m LIKE '%{termino}%' OR e.rut LIKE '%{termino}%' or concat(c.nivel, c.letra) like '%{termino}%'"
        parametros = {(termino, termino, termino, termino,)}
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def buscarAtrasoId(id):
        query = "SELECT e.nombres, e.apellido_p, e.apellido_m, c.nivel, c.letra, e.rut, e.avatar, a.fecha, a.hora, a.idatraso, a.idestudiante FROM atrasos a LEFT JOIN estudiante e ON a.idestudiante = e.idestudiante LEFT JOIN curso c ON e.idcurso = c.idcurso where a.idatraso = %s"
        parametros = (id,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado


    def crearAtraso(
        idestudiante,
        fecha,
        hora,
    ):
        query = "INSERT INTO atrasos (idestudiante, fecha, hora) VALUES (%s,%s,%s);"
        tipoConsulta = 1
        parametros = (idestudiante, fecha, hora,)
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
