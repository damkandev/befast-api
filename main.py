from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model.usuarios import Usuarios
from handler.usuarios import handleUsers 

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

# Raiz
@app.get("/api/")
def buscarUsuarios():
    return {"Hola":" Molto Deli"}

# Usuarios
@app.get("/api/usuarios")
def buscarUsuarios():
    usuarios = handleUsers.buscarUsuarios()
    return usuarios

@app.get("/api/usuario/{id}")
def buscarUsuario(id):
    usuarioBuscado = handleUsers.buscarUsuario()