from fastapi import FastAPI
from routes.cp_route import cp
from routes.banco_route import banco
from routes.ciudad_route import ciudad
from routes.empresa_route import empresa
from routes.usuario_route import usuario


from fastapi.middleware.cors import CORSMiddleware

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
app.include_router(ciudad)
app.include_router(empresa)
app.include_router(usuario)


@app.get("/")
def prim():
    return "Aplicacion funcionando en localHost"