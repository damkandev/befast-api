from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model.usuarios import Usuarios
from handler.usuarios import handleUsers


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/")
def raiz():
    return {"Hola": "BeFast"}


@app.post("/api/usuario")
async def registrarUsuario(request: Request):
    datos = await request.json()
    nombre = str()


@app.post("/api/login")
async def login(request: Request):
    datos = await request.json()
    correo = datos.get("correo")
    contrasena = datos.get("contrasena")
    resultado = Usuarios.iniciarSesion(correo, contrasena)
    return resultado
