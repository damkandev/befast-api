from connection.connection import Conecction


class cursos:
    def buscarCursos():
        query = "SELECT idcurso, nivel, letra FROM curso"
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta)
        conexionBD.desconectar()
        return resultado

    def buscarCurso(id):
        query = "SELECT idcurso, nivel, letra FROM curso WHERE idcurso = %s"
        parametros = (id,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def crearCurso(
        nivel,
        letra,
    ):
        query = "INSERT INTO curso (nivel, letra) VALUES (%s,%s);"
        tipoConsulta = 1
        parametros = (
            nivel,
            letra,
        )
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha insertado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la inserción", error)
        conexionBD.desconectar()

    def editarCurso(
        nivel,
        letra,
        idcurso,
    ):
        query = "UPDATE curso SET nivel = %s, letra =%s WHERE idcurso=%s;"
        tipoConsulta = 1
        parametros = (
            nivel,
            letra,
            idcurso,
        )
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha Editado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la edición", error)
        conexionBD.desconectar()

    def eliminarCurso(id):
        query = "DELETE FROM curso WHERE idcurso = %s;"
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
