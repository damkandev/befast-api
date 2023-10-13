from model.inspectores import inspectores


class handleInspectores:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def buscarInspectores():
        datos = inspectores.buscarInspectores()
        Inspectores = []
        for inspector in datos:
            _inspector = {
                "id": inspector[0],
                "nombres": inspector[1],
                "apellido_p": inspector[2],
                "apellido_m": inspector[3],
                "rut": inspector[4],
                "telefono": inspector[5],
                "direccion": inspector[6],
            }
            Inspectores.append(_inspector)
        return Inspectores

    def buscarInspector(id):
        inspectorBuscado = {}
        informacionInspector = inspectores.buscarInspector(id)
        for info in informacionInspector:
            inspectorBuscado = {
                "idinspector": info[0],
                "nombres": info[1],
                "apellido_p": info[2],
                "apellido_m": info[3],
                "rut": info[4],
                "telefono": info[5],
                "direccion": info[6],
            }
        return inspectorBuscado
