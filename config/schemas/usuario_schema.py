from datetime import date
from pydantic import BaseModel


class CrearUsuario(BaseModel):
    nombre = str
    apellido = str
    email = str
    password = str
    fecha_creacion = date
    proceso = str
    id = int


class Usuario(CrearUsuario):
    cedula: int

    class Config:
        orm_mode = True