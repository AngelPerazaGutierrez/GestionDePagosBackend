from datetime import datetime
from pydantic import BaseModel


class CrearUsuario(BaseModel):
    cedula = int
    nombre = str
    apellido = str
    email = str
    password = str
    fecha_creacion = datetime = datetime.now()
    proceso = str
    imagen = str


class Usuario(CrearUsuario):
    id: int

    class Config:
        orm_mode = True