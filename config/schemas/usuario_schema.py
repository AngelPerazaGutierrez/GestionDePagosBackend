from datetime import date
from pydantic import BaseModel


class CrearUsuario(BaseModel):
    cedula: int
    nombre: str
    apellido: str
    email: str
    password: str
    fecha_creacion: date
    proceso: str


class Usuario(CrearUsuario):
    id: int


    class Config:
        from_attributes = True