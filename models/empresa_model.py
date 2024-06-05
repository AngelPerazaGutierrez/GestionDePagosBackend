from sqlalchemy import String, Column, Integer, Enum
from GestionDePagosBackend.models.base import Base
from GestionDePagosBackend.enum.tipo_cuenta_enum import Tipo_Cuenta


class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    nit = Column(Integer, nullable=False)
    nombre_empresa = Column(String(100), nullable=False)
    tipo_cuenta1 = Column(Enum(Tipo_Cuenta), nullable=False, default='Ahorros')
    nombre_banco1 = Column(String(100), nullable=False)
    numero_cuenta1 = Column(Integer, nullable=False)
    ciudad = Column(String(100), nullable=False)
