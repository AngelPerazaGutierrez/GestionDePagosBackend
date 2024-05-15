from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from GestionDePagosBackend.config.db import Base

class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, index=True, nullable=False, autoincrement=True )
    nit = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50),nullable=False)

    # Relación con la tabla de bancos REVISAR LAS RELACIONES
    banco = relationship("Banco", back_populates="banco_info")
    tipo_cuenta = Column(Integer, nullable = False)
    numero_cuenta = Column(Integer, nullable = False)
    # Relación con la tabla de Ciudad
    ciudad = relationship("Ciudad", back_populates="")
