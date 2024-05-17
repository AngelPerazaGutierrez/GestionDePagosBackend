from pydantic import BaseModel

class CrearCiudad(BaseModel):
    pais: str
    ciudad: str

class Ciudad(CrearCiudad):
    id: int

    class Config:
        orm_mode = True

