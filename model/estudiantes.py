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

    def buscarEstudianteYApoderados(id):
        query = "select e.idestudiante, e.idcurso, e.nombres as estudiante_nombre, e.apellido_p as estudiante_apellido_p, e.apellido_m as estudiante_apellido_m, e.rut as estudiante_rut, e.telefono as estudiante_telefono, e.direccion as estudiante_direccion, e.idapoderado, e.idapoderadosup, e.avatar, a.nombres as apoderado_nombres, a.apellido_p as apoderado_apellido_p, a.apellido_m as apoderado_apellido_m, a.telefono as apoderado_telefono, a.rut as apoderado_rut, asup.nombres as apoderadosup_nombres, asup.apellido_p as apoderadosup_apellido_p, asup.apellido_m as idapoderadosup_apellido_m, asup.telefono as apoderadosup_telefono, asup.rut as apoderadosup_rut from estudiante e left join apoderado a on e.idapoderado = a.idapoderado left join apoderadosup asup on e.idapoderadosup = asup.idapoderadosup where idestudiante = %s"
        parametros = (id,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def buscarApoderadoPorRut(rut):
        query = "select idapoderado from apoderado where rut = %s"
        parametros = (rut,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def buscarApoderadoSupPorRut(rut):
        query = "select idapoderadosup from apoderadosup where rut = %s"
        parametros = (rut,)
        tipoConsulta = 2
        conexionBD = Conecction()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado

    def crearEstudiante(
        nombres,
        idcurso,
        apellido_p,
        apellido_m,
        rut,
        telefono,
        direccion,
        idapoderado,
        idapoderadosup,
        avatar,
    ):
        query = "INSERT INTO estudiante (nombres, idcurso, apellido_p,apellido_m,rut,telefono,direccion, idapoderado, idapoderadosup, avatar) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        tipoConsulta = 1
        parametros = (
            nombres,
            idcurso,
            apellido_p,
            apellido_m,
            rut,
            telefono,
            direccion,
            idapoderado,
            idapoderadosup,
            avatar,
        )
        conexionBD = Conecction()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha insertado Correctamente")
        except Exception as error:
            print("Ha ocurrido un problema en la inserción", error)
        conexionBD.desconectar()

    def editarEstudiante(
        nombres,
        idcurso,
        apellido_p,
        apellido_m,
        rut,
        telefono,
        direccion,
        idapoderado,
        idapoderadosup,
        avatar,
        idestudiante,
    ):
        query = "UPDATE befast.estudiante SET idcurso=%s, nombres=%s, apellido_p=%s, apellido_m=%s, rut=%s, telefono=%s, direccion=%s, idapoderado=%s, idapoderadosup=%s, avatar=%s WHERE idestudiante=%s;"
        tipoConsulta = 1
        parametros = (
            idcurso,
            nombres,
            apellido_p,
            apellido_m,
            rut,
            telefono,
            direccion,
            idapoderado,
            idapoderadosup,
            avatar,
            idestudiante,
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
