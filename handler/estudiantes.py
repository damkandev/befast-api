from model.estudiantes import estudiantes


class handleEstudiantes:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def buscarEstudiantes():
        datos = estudiantes.buscarEstudiantes()
        Estudiantes = []
        for estudiante in datos:
            _estudiante = {
                "id": estudiante[0],
                "idcurso": estudiante[1],
                "nombres": estudiante[2],
                "apellido_p": estudiante[3],
                "apellido_m": estudiante[4],
                "rut": estudiante[5],
                "telefono": estudiante[6],
                "direccion": estudiante[7],
            }
            Estudiantes.append(_estudiante)
        return Estudiantes

    def buscarEstudiante(id):
        estudianteBuscado = {}
        informacionEstudiante = estudiantes.buscarEstudiante(id)
        for info in informacionEstudiante:
            estudianteBuscado = {
                "nombres": info[0],
                "apellido_p": info[1],
                "apellido_m": info[2],
                "rut": info[3],
                "telefono": info[4],
                "direccion": info[5],
                "id": id,
            }
        return estudianteBuscado

    def buscarEstudianteYApoderados(id):
        estudianteYApoderadoBuscado = {}
        informacionEYA = estudiantes.buscarEstudianteYApoderados(id)
        for info in informacionEYA:
            estudianteYApoderadoBuscado = {
                "idestudiante": info[0],
                "idcurso": info[1],
                "estudiante_nombre": info[2],
                "estudiante_apellido_p": info[3],
                "estudiante_apellido_m": info[4],
                "estudiante_rut": info[5],
                "estudiante_telefono": info[6],
                "estudiante_direccion": info[7],
                "idapoderado": info[8],
                "idapoderadosup": info[9],
                "avatar": info[10],
                "apoderado_nombres": info[11],
                "apoderado_apellido_p": info[12],
                "apoderado_apellido_m": info[13],
                "apoderado_telefono": info[14],
                "apoderado_rut": info[15],
                "apoderadosup_nombres": info[16],
                "apoderadosup_apellido_p": info[17],
                "apoderadosup_apellido_m": info[18],
                "apoderadosup_telefono": info[19],
                "apoderadosup_rut": info[20],
            }
        return estudianteYApoderadoBuscado

    def buscarApoderadoPorRut(rut):
        apoderadoBuscado = {}
        informacionApoderado = estudiantes.buscarApoderadoPorRut(rut)
        for info in informacionApoderado:
            apoderadoBuscado = {"idapoderado": info[0]}
        return apoderadoBuscado

    def buscarApoderadoSupPorRut(rut):
        apoderadoSupBuscado = {}
        informacionApoderadoSup = estudiantes.buscarApoderadoSupPorRut(rut)
        for info in informacionApoderadoSup:
            apoderadoSupBuscado = {"idapoderadosup": info[0]}
        return apoderadoSupBuscado
