import enum
from pydantic import BaseModel


class CrearEmpresa(BaseModel):
    nombre_empresa: str
    tipo_cuenta1: str
    nombre_banco1: str
    numero_cuenta1: int
    ciudad: str


class Empresa(CrearEmpresa):
    nit: int

    class Config:
        orm_mode = True

