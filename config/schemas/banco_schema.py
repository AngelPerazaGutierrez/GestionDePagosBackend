from pydantic import BaseModel


class CrearBanco(BaseModel):
    tipo_cuenta: str
    nit: int
    banco_info_nit: int
    banco_info: str


class Banco(CrearBanco):
    id: int

    class Config:
        orm_mode = True