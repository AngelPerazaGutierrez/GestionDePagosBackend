from sqlalchemy import String, Column, Integer, Enum
from GestionDePagosBackend.models.base import Base
from GestionDePagosBackend.enum.tipo_cuenta_enum import Tipo_Cuenta


class Banco(Base):
    __tablename__ = "banco"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    nit = Column(Integer, primary_key=True, index=True, nullable=False)
    tipo_cuenta = Column(Enum(Tipo_Cuenta), nullable=False, default='Ahorros')
    nombre_banco = Column(String(100), nullable=False)



