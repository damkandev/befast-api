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
            }
        return estudianteBuscado
