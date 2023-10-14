from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model.usuarios import Usuarios
from model.estudiantes import estudiantes
from model.inspectores import inspectores
from model.cursos import cursos
from model.atrasos import atrasos
from model.apoderados import apoderados
from model.apoderadosup import apoderadosSUp
from handler.apoderadosup import handleApoderadosSup
from handler.apoderados import handleApoderados
from handler.usuarios import handleUsers
from handler.estudiantes import handleEstudiantes
from handler.inspectores import handleInspectores
from handler.cursos import handleCursos
from handler.atrasos import handleAtrasos


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Raiz
@app.get("/api/")
def raiz():
    return {"Hola": "BeFast"}


# Registrar Usuario
@app.post("/api/usuario")
async def registrarUsuario(request: Request):
    datos = await request.json()
    nombre = str()


# Inicio de Sesión
@app.post("/api/login")
async def login(request: Request):
    datos = await request.json()
    correo = datos.get("correo")
    contrasena = datos.get("contrasena")
    resultado = Usuarios.iniciarSesion(correo, contrasena)
    return resultado


# Estudiantes
@app.get("/api/estudiantes")
def buscarEstudiantes():
    estudiantes = handleEstudiantes.buscarEstudiantes()
    return estudiantes


@app.get("/api/estudiante/{id}")
def buscarEstudiante(id):
    estudianteBuscado = handleEstudiantes.buscarEstudiante(id)
    return estudianteBuscado


@app.get("/api/estudianteyapoderado/{id}")
def buscarEYA(id):
    eyabuscado = handleEstudiantes.buscarEstudianteYApoderados(id)
    return eyabuscado


@app.post("/api/estudiante")
async def crearEstudiante(request: Request):
    datos = await request.json()
    nombres = str(datos["nombres"])
    idcurso = int(datos["idcurso"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    rut = int(datos["rut"])
    telefono = int(datos["telefono"])
    direccion = str(datos["direccion"])
    idapoderado = int(datos["idapoderado"])
    idapoderadosup = int(datos["idapoderadosup"])
    avatar = str(datos["avatar"])
    print(datos)
    print(
        estudiantes.crearEstudiante(
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
    )
    return datos


@app.put("/api/estudiante/{id}")
async def editarEstudiante(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    nombres = str(datos["nombres"])
    idcurso = int(datos["idcurso"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    rut = int(datos["rut"])
    telefono = int(datos["telefono"])
    direccion = str(datos["direccion"])
    idapoderado = str(datos["idapoderado"])
    idapoderadosup = str(datos["idapoderadosup"])
    avatar = str(datos["avatar"])
    print(
        estudiantes.editarEstudiante(
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
            _id,
        )
    )
    return datos


@app.delete("/api/estudiante/{id}")
async def eliminarEstudiante(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    print(estudiantes.eliminarEstudiante(_id))


# Inspectores
@app.get("/api/inspectores")
def buscarInspectores():
    inspectores = handleInspectores.buscarInspectores()
    return inspectores


@app.get("/api/inspector/{id}")
def buscarInspector(id):
    inspectorBuscado = handleInspectores.buscarInspector(id)
    return inspectorBuscado


@app.post("/api/inspector")
async def crearInspector(request: Request):
    datos = await request.json()
    nombres = str(datos["nombres"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    rut = int(datos["rut"])
    telefono = int(datos["telefono"])
    direccion = str(datos["direccion"])
    print(
        inspectores.crearInspector(
            nombres, apellido_p, apellido_m, rut, telefono, direccion
        )
    )
    return datos


@app.put("/api/inspector/{id}")
async def editarInspector(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    nombres = str(datos["nombres"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    rut = int(datos["rut"])
    telefono = int(datos["telefono"])
    direccion = str(datos["direccion"])
    print(
        inspectores.editarInspector(
            nombres, apellido_p, apellido_m, rut, telefono, direccion, _id
        )
    )
    return datos


@app.delete("/api/inspector/{id}")
async def eliminarEstudiante(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    print(inspectores.eliminarInspector(_id))


# Apoderados
@app.get("/api/apoderados")
def buscarApoderados():
    apoderados = handleApoderados.buscarApoderados()
    return apoderados


@app.get("/api/apoderado/{id}")
def buscarApoderado(id):
    apoderadoBuscado = handleApoderados.buscarApoderado(id)
    return apoderadoBuscado


@app.post("/api/apoderado")
async def crearApoderado(request: Request):
    datos = await request.json()
    nombres = str(datos["nombres"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    telefono = int(datos["telefono"])
    rut = int(datos["rut"])
    print(datos)
    print(
        apoderados.crearApoderado(
            nombres,
            apellido_p,
            apellido_m,
            telefono,
            rut,
        )
    )
    return datos


@app.put("/api/apoderado/{id}")
async def editarApoderado(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    nombres = str(datos["nombres"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    telefono = str(datos["telefono"])
    rut = int(datos["rut"])
    print(
        apoderados.editarApoderado(
            nombres,
            apellido_p,
            apellido_m,
            rut,
            telefono,
            _id,
        )
    )
    return datos


@app.delete("/api/apoderado/{id}")
async def eliminarApoderado(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    print(apoderados.eliminarApoderado(_id))


# Apoderados Suplentes
@app.get("/api/apoderadossup")
def buscarApoderadosSup():
    apoderadosSup = handleApoderadosSup.buscarApoderadosSup()
    return apoderadosSup


@app.get("/api/apoderadosup/{id}")
def buscarApoderadoSup(id):
    apoderadoBuscadoSup = handleApoderadosSup.buscarApoderadoSup(id)
    return apoderadoBuscadoSup


@app.post("/api/apoderadosup")
async def crearApoderadoSup(request: Request):
    datos = await request.json()
    nombres = str(datos["nombres"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    telefono = int(datos["telefono"])
    rut = int(datos["rut"])
    print(datos)
    print(
        apoderadosSUp.crearApoderadoSup(
            nombres,
            apellido_p,
            apellido_m,
            telefono,
            rut,
        )
    )
    return datos


@app.put("/api/apoderadosup/{id}")
async def editarApoderado(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    nombres = str(datos["nombres"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    telefono = str(datos["telefono"])
    rut = int(datos["rut"])
    print(
        apoderadosSUp.editarApoderadoSup(
            nombres,
            apellido_p,
            apellido_m,
            rut,
            telefono,
            _id,
        )
    )
    return datos


@app.delete("/api/apoderadosup/{id}")
async def eliminarApoderado(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    print(apoderadosSUp.eliminarApoderadoSup(_id))


# busqueda por rut
@app.get("/api/apoderadorut/{rut}")
def buscarApoderadoRut(rut):
    apoderado = handleEstudiantes.buscarApoderadoPorRut(rut)
    return apoderado


@app.get("/api/apoderadosuprut/{rut}")
def buscarApoderadoSupRut(rut):
    apoderadosup = handleEstudiantes.buscarApoderadoSupPorRut(rut)
    return apoderadosup


# Cursos
@app.get("/api/cursos")
def buscarCursos():
    cursos = handleCursos.buscarCursos()
    return cursos


@app.get("/api/curso/{id}")
def buscarCurso(id):
    cursoBuscado = handleCursos.buscarCurso(id)
    return cursoBuscado


@app.put("/api/curso/{id}")
async def editarCurso(request: Request):
    datos = await request.json()
    _id = int(datos["idcurso"])
    nivel = int(datos["nivel"])
    letra = str(datos["letra"])
    print(cursos.editarCurso(nivel, letra, _id))
    return datos


@app.post("/api/cursos")
async def crearCurso(request: Request):
    datos = await request.json()
    nivel = int(datos["nivel"])
    letra = str(datos["letra"])
    print(cursos.crearCurso(nivel, letra))
    return datos


@app.delete("/api/curso/{id}")
async def eliminarCurso(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    print(cursos.eliminarCurso(_id))


# Atrasos
@app.get("/api/atrasos")
def buscarAtrasos():
    atrasos = handleAtrasos.buscarAtrasos()
    return atrasos

@app.get("/api/atraso/{term}")
def buscarAtraso(term):
    atrasos = handleAtrasos.buscarAtraso(term)
    return atrasos

