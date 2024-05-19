from pydantic import BaseModel


class CrearBanco(BaseModel):
    tipo_cuenta: str
    nombre_banco: str

class Banco(CrearBanco):
    nit: int
    #luego hacer verificacion de nits + enums, que no esten reepetidos para no hacer duplicados

    class Config:
        orm_mode = True