from pydantic import BaseModel


class CrearBanco(BaseModel):
    nit: int
    tipo_cuenta: str
    nombre_banco: str


class Banco(CrearBanco):
    id: int

    class Config:
        orm_mode = True
