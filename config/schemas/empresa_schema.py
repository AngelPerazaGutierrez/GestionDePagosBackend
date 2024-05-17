from pydantic import BaseModel

class CrearEmpresa(BaseModel):
    nit: int
    nombre: str
    banco: str
    tipo_cuenta: str
    numero_cuenta: int
    ciudad: str

class Empresa(CrearEmpresa):
    id: int

    class Config:
        orm_mode = True

