from datetime import date
from pydantic import BaseModel


class CrearCp(BaseModel):
    adjuntos: str
    fecha: date
    ciudad: str
    nit: int
    tercero: str
    concepto: str
    banco: str
    tipo_cuenta: str
    numero_cuenta: int
    valor: int


class Cp(CrearCp):
    id: int

    class Config:
        from_attributes = True



