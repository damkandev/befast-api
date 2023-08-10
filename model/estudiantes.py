from connection.connection import Conecction


class estudiantes:
    def buscarEstudiantes():
        query = "SELECT idestudiante, idcurso, nombres, apellido_p , apellido_m, rut, telefono, direccion FROM estudiante"
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta)
        conexionBD.desconectar()
        return resultado

    def buscarEstudiante(id):
        query = "SELECT  nombres, apellido_p, apellido_m, rut, telefono, direccion FROM estudiante WHERE idestudiante = %s"
        parametros = (id,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def crearEstudiante(nombres, apellido_p, apellido_m, rut, telefono, direccion):
        query = "INSERT INTO estudiante (nombres,apellido_p,apellido_m,rut,telefono,direccion) VALUES (%s,%s,%s,%s,%s,%s);"
        tipoConsulta = 1
        parametros = nombres, apellido_p, apellido_m, rut, telefono, direccion
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha insertado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la inserción", error)
        conexionBD.desconectar()

    def editarEstudiante(nombres, apellido_p, apellido_m, rut, telefono, direccion, id):
        print(nombres, apellido_p, apellido_m, rut, telefono, direccion, id)
        query = "UPDATE estudiante SET nombres=%s,apellido_p=%s,apellido_m=%s,rut=%s,telefono=%s,direccion=%s WHERE idestudiante = %s;"
        tipoConsulta = 1
        parametros = (
            nombres,
            apellido_p,
            apellido_m,
            rut,
            telefono,
            direccion,
            id,
        )
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha Editado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la edición", error)
        conexionBD.desconectar()

    def eliminarEstudiante(id):
        query = "DELETE FROM estudiante WHERE idestudiante = %s;"
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
