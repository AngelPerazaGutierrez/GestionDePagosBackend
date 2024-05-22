from pydantic import BaseModel


class CrearCiudad(BaseModel):
    pais: str
    ciudadnombre: str


class Ciudad(CrearCiudad):
    id: int

    class Config:
        from_attributes = True

