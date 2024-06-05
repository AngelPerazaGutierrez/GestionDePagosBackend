from pydantic import BaseModel


class CrearEmpresa(BaseModel):
    nit: int
    nombre_empresa: str
    tipo_cuenta1: str
    nombre_banco1: str
    numero_cuenta1: int
    ciudad: str


class Empresa(CrearEmpresa):
    id: int

    class Config:
        from_attributes = True

