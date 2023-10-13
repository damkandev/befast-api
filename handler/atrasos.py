from model.atrasos import atrasos


class handleAtrasos:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def buscarAtrasos():
        datos = atrasos.buscarAtrasos()
        Atrasos = []
        for atraso in datos:
            _atraso = {
                "idestudiante": atraso[0],
                "nombres": atraso[1],
                "apellido_p": atraso[2],
                "apellido_m": atraso[3],
                "avatar": atraso[4],
                "nivel": atraso[5],
                "letra": atraso[6],
                "rut": atraso[7],
                "fecha_atraso": atraso[8],
                "hora_atraso": atraso[9],
            }
            Atrasos.append(_atraso)
        return Atrasos

    def buscarAtraso(id):
        atrasoBuscado = {}
        informacionAtraso = atrasos.buscarAtraso(id)
        for info in informacionAtraso:
            atrasoBuscado = {
                "idestudiante": info[0],
                "nombres": info[1],
                "apellido_p": info[2],
                "apellido_m": info[3],
                "avatar": info[4],
                "nivel": info[5],
                "letra": info[6],
                "rut": info[7],
                "fecha_atraso": info[8],
                "hora_atraso": info[9],
            }
        return atrasoBuscado
