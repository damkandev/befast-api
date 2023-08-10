from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model.usuarios import Usuarios
from model.estudiantes import estudiantes
from model.inspectores import inspectores
from handler.usuarios import handleUsers
from handler.estudiantes import handleEstudiantes
from handler.inspectores import handleInspectores


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


@app.post("/api/estudiante")
async def crearEstudiante(request: Request):
    datos = await request.json()
    nombres = str(datos["nombres"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    rut = int(datos["rut"])
    telefono = int(datos["telefono"])
    direccion = str(datos["direccion"])
    print(
        estudiantes.crearEstudiante(
            nombres, apellido_p, apellido_m, rut, telefono, direccion
        )
    )
    return datos


@app.put("/api/estudiante/{id}")
async def editarEstudiante(request: Request):
    datos = await request.json()
    _id = int(datos["id"])
    nombres = str(datos["nombres"])
    apellido_p = str(datos["apellido_p"])
    apellido_m = str(datos["apellido_m"])
    rut = int(datos["rut"])
    telefono = int(datos["telefono"])
    direccion = str(datos["direccion"])
    print(
        estudiantes.editarEstudiante(
            nombres, apellido_p, apellido_m, rut, telefono, direccion, _id
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
