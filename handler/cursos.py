from model.cursos import cursos


class handleCursos:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def buscarCursos():
        datos = cursos.buscarCursos()
        Cursos = []
        for curso in datos:
            _curso = {
                "idcurso": curso[0],
                "nivel": curso[1],
                "letra": curso[2],
            }
            Cursos.append(_curso)
        return Cursos

    def buscarCurso(id):
        cursoBuscado = {}
        informacionCurso = cursos.buscarCurso(id)
        for info in informacionCurso:
            cursoBuscado = {
                "idcurso": info[0],
                "nivel": info[1],
                "letra": info[2],
            }
        return cursoBuscado
