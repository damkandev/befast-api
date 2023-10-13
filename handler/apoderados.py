from model.apoderados import apoderados


class handleApoderados:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def buscarApoderados():
        datos = apoderados.buscarApoderados()
        Apoderados = []
        for apoderado in datos:
            _apoderado = {
                "idapoderado": apoderado[0],
                "nombres": apoderado[1],
                "apellido_p": apoderado[2],
                "apellido_m": apoderado[3],
                "telefono": apoderado[4],
                "rut": apoderado[5],
            }
            Apoderados.append(_apoderado)
        return Apoderados

    def buscarApoderado(id):
        apoderadoBuscado = {}
        informacionApoderado = apoderados.buscarApoderado(id)
        for info in informacionApoderado:
            apoderadoBuscado = {
                "idapoderado": info[0],
                "nombres": info[1],
                "apellido_p": info[2],
                "apellido_m": info[3],
                "telefono": info[4],
                "rut": info[5],
            }
        return apoderadoBuscado
