from sqlalchemy import Enum, String, Column, Integer, Date, Text
from GestionDePagosBackend.config.db import Base
from GestionDePagosBackend.enum.procesos_enum import Procesos


class Usuario(Base):
   __tablename__ = "usuario"
   id = Column(Integer(11), index=True, nullable=False, autoincrement=True, primary_key=True)
   cedula = Column(Integer(11))
   nombre = Column(String, nullable=False)
   apellido = Column(String, nullable=False)
   email = Column(String, nullable=False)
   password = Column(String, nullable=False)
   fecha_creacion = Column(Date, nullable=False)
   proceso = Column(Enum(Procesos), nullable=False)

