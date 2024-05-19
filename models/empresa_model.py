from sqlalchemy import String, Column, Integer, Enum
from sqlalchemy.orm import relationship
from GestionDePagosBackend.config.db import Base
from GestionDePagosBackend.enum.tipo_cuenta_enum import Tipo_Cuenta


class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, index=True, nullable=False, autoincrement=True )
    nit = Column(Integer, primary_key=True, nullable=False)
    nombre_empresa = Column(String(50), nullable=False)
    tipo_cuenta1 = Column(Enum(Tipo_Cuenta), nullable=False)
    nombre_banco1 = Column(String, nullable=False)
    numero_cuenta1 = Column(Integer, nullable=False)
    ciudad = Column(String, nullable=False)
