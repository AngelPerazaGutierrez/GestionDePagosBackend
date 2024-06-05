from fastapi import FastAPI
from routes.cp_route import cp
from routes.banco_route import banco
from routes.empresa_route import empresa
from routes.usuario_route import usuario
from fastapi.middleware.cors import CORSMiddleware
from GestionDePagosBackend.config.db import SessionLocal
import crearInstancias
from sqlalchemy.exc import IntegrityError


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(cp)
app.include_router(banco)
app.include_router(empresa)
app.include_router(usuario)

session = SessionLocal()
session.add(crearInstancias.nuevo_banco)
session.add(crearInstancias.nuevo_comprobante)
session.add(crearInstancias.nueva_empresa)
try:
    session.add(crearInstancias.nuevo_usuario)
    session.commit()
except IntegrityError:
    session.rollback()
    print(f"El usuario con cédula {crearInstancias.nuevo_usuario.cedula} ya existe. No se puede duplicar.")
session.commit()


@app.get("/")
def test():
    return "Aplicacion funcionando en localHost"