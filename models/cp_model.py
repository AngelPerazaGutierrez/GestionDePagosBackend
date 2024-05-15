from sqlalchemy import String, Column, Integer, Date, LargeBinary
from GestionDePagosBackend.config.db import Base


class Cp(Base):
    __tablename__ = "cp"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    adjuntos = Column(LargeBinary, nullable=False)
    fecha = Column(Date, nullable=False)
    ciudad = Column(nullable=False)
    nit = Column(Integer, nullable=False)
    tercero = Column(nullable=False)
    concepto = Column(String, nullable=False)
    banco = Column(nullable=False)
    tipo_cuenta = Column(nullable=False)
    numero_cuenta = Column(nullable=False)
    valor = Column(Integer, nullable=False)
