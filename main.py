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


# Raiz
@app.get("/api/")
def raiz():
    return {"Hola": " Molto Deli"}


@app.post("/api/usuario")
async def registrarUsuario(request: Request):
    datos = await request.json()
    nombre = str()
