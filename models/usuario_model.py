from sqlalchemy import String, Column, Integer, Date, Enum
from GestionDePagosBackend.config.db import Base
from GestionDePagosBackend.enum.procesos_enum import Procesos


class Usuario(Base):
   __tablename__ = "usuario"
   id = Column(Integer, index=True, nullable=False, autoincrement=True, primary_key=True)
   cedula = Column(Integer, nullable=False)
   nombre = Column(nullable=False)
   apellido = Column(nullable=False)
   email = Column(String, nullable=False)
   password = Column(String, nullable=False)
   fecha_creacion = Column(Date, nullable=False)
   proceso = Column(Enum(Procesos), nullable=False)

