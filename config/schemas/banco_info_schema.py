from datetime import datetime
from pydantic import BaseModel

class CrearBancoInfo(BaseModel):
    nit: int
    nombre: str
    banco: str

class BancoInfo(CrearBancoInfo):
    id: int

    class Config:
        orm_mode = True