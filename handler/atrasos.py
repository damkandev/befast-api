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
                "nombres": atraso[0],
                "apellido_p": atraso[1],
                "apellido_m": atraso[2],
                "nivel": atraso[3],
                "letra": atraso[4],
                "rut": atraso[5],
                "avatar":atraso[6],
                "fecha": atraso[7],
                "hora": atraso[8],
                "idatraso": atraso[9],
                "idestudiante": atraso[10],
            }
            Atrasos.append(_atraso)
        return Atrasos
    
    def buscarAtraso(termino):
        datos = atrasos.buscarAtraso(termino)
        Atrasos = []
        for atraso in datos:
            _atraso = {
                "nombres": atraso[0],
                "apellido_p": atraso[1],
                "apellido_m": atraso[2],
                "nivel": atraso[3],
                "letra": atraso[4],
                "rut": atraso[5],
                "avatar":atraso[6],
                "fecha": atraso[7],
                "hora": atraso[8],
                "idatraso": atraso[9],
                "idestudiante": atraso[10],
            }
            Atrasos.append(_atraso)
        return Atrasos
