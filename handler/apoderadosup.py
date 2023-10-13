from model.apoderadosup import apoderadosSUp


class handleApoderadosSup:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def buscarApoderadosSup():
        datos = apoderadosSUp.buscarApoderadosSup()
        ApoderadosSup = []
        for apoderadosup in datos:
            _apoderadosup = {
                "idapoderado": apoderadosup[0],
                "nombres": apoderadosup[1],
                "apellido_p": apoderadosup[2],
                "apellido_m": apoderadosup[3],
                "telefono": apoderadosup[4],
                "rut": apoderadosup[5],
            }
            ApoderadosSup.append(_apoderadosup)
        return ApoderadosSup

    def buscarApoderadoSup(id):
        apoderadoBuscadoSup = {}
        informacionApoderadoSup = apoderadosSUp.buscarApoderadoSup(id)
        for info in informacionApoderadoSup:
            apoderadoBuscadoSup = {
                "idapoderado": info[0],
                "nombres": info[1],
                "apellido_p": info[2],
                "apellido_m": info[3],
                "telefono": info[4],
                "rut": info[5],
            }
        return apoderadoBuscadoSup
