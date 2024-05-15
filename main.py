from fastapi import FastAPI
from routes.cp_route import cp

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(cp)



@app.get("/")
def prim():
    return "Aplicacion funcionando en '/' "