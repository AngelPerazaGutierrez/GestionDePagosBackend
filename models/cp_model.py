from sqlalchemy import String, Column, Integer, Date
from GestionDePagosBackend.models.base import Base


class Cp(Base):
    __tablename__ = "cp"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    adjuntos = Column(String(100), nullable=True)
    fecha = Column(Date, nullable=False)
    ciudad = Column(String(100), nullable=False)
    nit = Column(Integer, nullable=False)
    tercero = Column(String(100), nullable=False)
    concepto = Column(String(100), nullable=False)
    banco = Column(String(100), nullable=False)
    tipo_cuenta = Column(String(100), nullable=False)
    numero_cuenta = Column(Integer, nullable=False)
    valor = Column(Integer, nullable=False)


