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


test = Usuarios.iniciarSesion("juan@gmail.com", "jfihfuhsdf")
print(test)
