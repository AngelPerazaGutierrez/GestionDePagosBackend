from sqlalchemy import String, Column, Integer, Enum
from GestionDePagosBackend.config.db import Base
from GestionDePagosBackend.enum.tipo_cuenta_enum import Tipo_Cuenta


class Banco(Base):
    __tablename__ = "banco"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    nit = Column(Integer, primary_key=True, index=True, nullable=False)
    tipo_cuenta = Column(Enum(Tipo_Cuenta), nullable=False)
    nombre_banco = Column(String, nullable=False)



